# Ore - A package manager for Oranje
import sys
import requests
from tqdm import tqdm

if len(sys.argv) > 1:
    repo = sys.argv[1]
    branch = sys.argv[2] if (len(sys.argv)>2) else "main"
else: sys.exit()

url = f'https://github.com/{repo}/archive/refs/heads/{branch}.zip'
filename = f'./package/{repo}.zip'

response = requests.get(url, stream=True)
file_size = int(response.headers.get("Content-Length", 0))

with open(filename, "wb") as f:
    with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as progress:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                progress.update(len(chunk))
print("Download complete!")
