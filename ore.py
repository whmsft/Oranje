# Ore v0.2 - A package manager for Oranje
import os
import sys
import time
import fire
import shutil
import zipfile
import requests
import tempfile
import itertools
import threading
from tqdm import tqdm

ANIMATE = False
ANIMATE_TEXT = "Working Online"
TEMP = tempfile.gettempdir()
PROGRAM_DIR = os.path.dirname(os.path.realpath(__file__))


def loadingAnimator():
    global ANIMATE, ANIMATE_TEXT
    for state in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
        if ANIMATE:
            sys.stdout.write(f'\r{ANIMATE_TEXT} ' + state)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r')


class Ore:
    animationThread = threading.Thread(target=loadingAnimator)
    animationThread.daemon = True
    animationThread.start()

    def install(self, repo="whmsft/oranje", branch="main", dir=""):
        global ANIMATE, ANIMATE_TEXT, animationThread
        ANIMATE = True
        url = f'https://github.com/{repo}/archive/refs/heads/{branch}.zip'
        filename = f'{TEMP}/{repo.split("/")[1]}.zip'
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get("Content-Length", 0))
        ANIMATE = False
        with open(filename, "wb") as f:
            with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as progress:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        progress.update(len(chunk))
        with zipfile.ZipFile(filename) as archive:
            archive.extractall(f'{TEMP}/{repo}')
        print(f'{TEMP}/{repo}/{repo.split("/")[1].lower()}-{branch}/{dir}')
        shutil.copytree(f'{TEMP}/{repo}/{repo.split("/")[1].lower()}-{branch}/{dir}', f'{PROGRAM_DIR}/package/{repo}/')
        print(f"\nInstalled {repo} from GitHub")


if __name__ == "__main__":
    fire.Fire(Ore)
