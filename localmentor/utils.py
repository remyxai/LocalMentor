import os
import requests

def download_mentor():
    bin_dir = os.path.join(os.path.dirname(__file__), 'bin')
    mentor_path = os.path.join(bin_dir, 'mentor')

    # Create the 'bin/' directory if it does not exist
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir, exist_ok=True)

    # Download mentor file if it does not exist
    if not os.path.exists(mentor_path):
        print("Downloading mentor...")
        model_url = "https://remyx.ai/assets/localmentor/0.0.1/mentor"
        response = requests.get(model_url, stream=True)
        with open(mentor_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Make the file executable
        os.chmod(mentor_path, 0o755)

        print("Download complete.")
