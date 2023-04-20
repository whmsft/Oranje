import os
import chlorophyll
import tklinenums
import tkinter as tk
from tkinter import ttk

cwd = os.getcwd()

PACKAGE = {}

for author in os.listdir(cwd+"/package"): PACKAGE[author] = []
for author in PACKAGE.keys(): 
    for package in os.listdir(cwd+"/package/"+author): PACKAGE[author].append(package)
print(PACKAGE)