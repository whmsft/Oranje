import os
import tkinter as tk
from tkinter import ttk

cwd = os.getcwd()
pdir = os.path.dirname(os.path.realpath(__file__))

PACKAGE = {}

if __name__ == "__main__":
	for author in os.listdir(f'{pdir}/package'):
		if os.path.isdir(f'{pdir}/package/{author}'):
			PACKAGE[author] = []
	for author in PACKAGE.keys():
		for package in os.listdir(f'{pdir}/package/{author}'):
			if (os.path.isdir(f'{pdir}/package/{author}/{package}')):
				PACKAGE[author].append(package)
				exec(f'import package.{author}.{package}')
	for officialPackage in PACKAGE['whmsft']:
		exec(f'{officialPackage}.init()')
	packagesTemporary = PACKAGE.pop()
	packagesTemporary.pop('whmsft')
	del author, package, packagesTemporary