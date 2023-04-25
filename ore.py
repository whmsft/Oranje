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
lualipa = 2**24
with alive_bar(lualipa, title="[RET]") as bar:
    while lualipa != 0:
        bar()
        lualipa -= 1