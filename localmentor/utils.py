import hashlib
import os
import sys
import requests

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

    # Expected SHA1 hash of the remote mentor file
    expected_hash = "6dfab6acf5c33e89e52492f1865eb57d84667e77"

    # Create the 'bin/' directory if it does not exist
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir, exist_ok=True)

    # Check if the file exists and its hash
    if os.path.exists(mentor_path):
        local_hash = calculate_sha1(mentor_path)
        if local_hash == expected_hash:
            return
        else:
            print("Unexpected mentor found. Redownloading...")

    model_url = "https://remyx.ai/assets/localmentor/0.0.1/mentor"
    response = requests.get(model_url, stream=True)

    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 8192
    downloaded = 0

    with open(mentor_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            downloaded += len(chunk)
            percentage = 100 * downloaded // total_size
            sys.stdout.write(f'\rDownloading mentor... {percentage}%')
            sys.stdout.flush()

    # Make the file executable
    os.chmod(mentor_path, 0o755)

    print("\nDownload complete.")
