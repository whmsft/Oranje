# Ore - A package manager for Oranje
import requests
from tqdm import tqdm

# The URL of the GitHub repository to download
url = "https://github.com/whmsft/oranje/archive/refs/heads/main.zip"

# The path and filename to save the downloaded file to
filename = "oranje.zip"

# Send a GET request to the URL and get the content length of the response
response = requests.get(url, stream=True)
file_size = int(response.headers.get("Content-Length", 0))

# Create a tqdm progress bar and start downloading the file
with open(filename, "wb") as f:
    with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as progress:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                # Write the downloaded data to the file and update the progress bar
                f.write(chunk)
                progress.update(len(chunk))

# Print a message to indicate that the download is complete
print("Download complete!")
