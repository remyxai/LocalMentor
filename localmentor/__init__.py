import shlex
import subprocess
import pkg_resources

from .utils import download_mentor

def mentor(prompt):
    download_mentor()
    mentor_path = pkg_resources.resource_filename('localmentor', 'bin/mentor')
    safe_prompt = shlex.quote(prompt)
    command = '{} -p "{}"'.format(mentor_path, safe_prompt)

    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return None
