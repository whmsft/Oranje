# Ore - A package installer for Oranje.
import time
import fsspec
from pathlib import Path
from alive_progress import alive_bar

"""#destination.mkdir(exist_ok=True, parents=True)
fs = fsspec.filesystem("github", org="whmsft", repo="oranje")
print("[Loaded filesystem]")
print(fs.ls("package"))
print("[Loaded folder]")
fs.get("package/whmsft", 'pp/', recursive=True)"""
packtitle = "whmsft/oranje"
dirpath = "@package/whmsft/oranje"
f = 2**250
with alive_bar(f, title="[GET] (github) {}") as bar:
    while f != 0:
        bar()
        f -= 1
