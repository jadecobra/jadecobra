import sniffer.api
import subprocess
watch_paths = ['tests/', 'src/']

@sniffer.api.runnable
def run_tests(*args):
    if not subprocess.run(
        'python -m unittest -f tests/*.*',
        shell=True
    ).returncode:
        return False
    return True