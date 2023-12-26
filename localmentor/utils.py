import os
import sys
import requests
import hashlib

def calculate_sha1(filepath):
    sha1 = hashlib.sha1()
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def download_mentor():
    bin_dir = os.path.join(os.path.dirname(__file__), 'bin')
    mentor_path = os.path.join(bin_dir, 'mentor')
    hash_path = os.path.join(bin_dir, 'mentor.hash')

    # Hardcoded hash for the latest mentor
    hardcoded_hash = "6dfab6acf5c33e89e52492f1865eb57d84667e77"

    # Check if mentor.hash exists and matches the hardcoded hash
    # Here so localmentor works offline 
    if os.path.exists(hash_path):
        with open(hash_path, 'r') as hash_file:
            local_hash = hash_file.read().strip()
            if local_hash == hardcoded_hash:
                return  # File is up to date, no need to download

    model_url = "https://remyx.ai/assets/localmentor/0.0.1/mentor"
    # Perform a HEAD request to get the size of the remote mentor file
    response = requests.head(model_url)
    remote_size = int(response.headers.get('content-length', 0))

    # Check if the local mentor is the same size as the remote mentor
    if os.path.exists(mentor_path):
        local_size = os.path.getsize(mentor_path)
        if local_size == remote_size:
            return

    # If the sizes do not match, or the file does not exist, start/resume download
    headers = {}
    if os.path.exists(mentor_path):
        downloaded_size = os.path.getsize(mentor_path)
        headers['Range'] = f'bytes={downloaded_size}-'
    else:
        downloaded_size = 0

    response = requests.get(model_url, headers=headers, stream=True)
    total_size = remote_size

    with open(mentor_path, 'ab') as f:  # Append to the file if it exists
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded_size += len(chunk)
            percentage = 100 * downloaded_size // total_size
            sys.stdout.write(f'\rDownloading mentor... {percentage}%')
            sys.stdout.flush()

    # Make the file executable
    os.chmod(mentor_path, 0o755)

    # Calculate and write the SHA-1 hash of the downloaded file
    file_hash = calculate_sha1(mentor_path)
    with open(hash_path, 'w') as hash_file:
        hash_file.write(file_hash)

    # Clear the line after the download is complete
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()
