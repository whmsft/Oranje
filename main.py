import os
import yaml
import tkinter as tk
from tkinter import ttk
from package.whmsft import oranje

cwd = os.getcwd()
pdir = os.path.dirname(os.path.realpath(__file__))

PACKAGE = {}
"""
How the "PACKAGE" dict will look like:
PACKAGE = {
	'whmsft': [
		'oranje': {
			'author': {
				'name': 'whmsft',
				'email': 'whmsft@outlook.com'
			},
			'package': {
				'name': 'Oranje Editor',
  				'url': 'https://github.com/whmsft/Oranje',
  				'version': [0, 0, 1]
			}
		}
	]
}
"""

if __name__ == "__main__":
	for author in os.listdir(f'{pdir}/package'):
		if os.path.isdir(f'{pdir}/package/{author}'):
			PACKAGE[author] = []
	for author in PACKAGE.keys():
		for pack in os.listdir(f'{pdir}/package/{author}'):
			if (os.path.isdir(f'{pdir}/package/{author}/{pack}')):
				if not (author == "whmsft" and pack == "oranje"):
					PACKAGE[author].append(pack)
					exec(f'import package.{author}.{pack}')
	del author, pack

	oranje.init()
	