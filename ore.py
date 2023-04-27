# Ore - A package manager for Oranje
import fire
import requests
from tqdm import tqdm

class Ore:
    def gh(self, repo="whmsft/oranje", branch="main", dir="."):
        url = f'https://github.com/{repo}/archive/refs/heads/{branch}.zip'
        filename = f'./{repo.split("/")[1]}.zip'
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get("Content-Length", 0))

        with open(filename, "wb") as f:
            with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as progress:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        progress.update(len(chunk))
        print("Download complete!")

if __name__ == "__main__":
    fire.Fire(Ore)