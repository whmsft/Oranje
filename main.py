import tkinter as tk
import pygments.lexers
from tkinter import ttk
from chlorophyll import CodeView
from widgets.texteditor import ScrollCode

def tabupd():
  for x in cbuttons: x.config(bg="#020203")
  for x in tbuttons: x.config(bg="#020203")
  tbuttons[seltab.get()].config(bg = "#0a0e14")
  cbuttons[seltab.get()].config(bg = "#0a0e14")
  root.after(100, tabupd)

def newtab():
  global totbutts
  tbuttons.append(tk.Button(tabbar, font = "Consolas 13",text = " Untitled ", relief="flat", fg="#b3b1ad", bg="#020203", activebackground="#1b2733", borderwidth=0, command=lambda i=totbutts:seltab.set(i)))
  tbuttons[-1].pack(side = "left", padx = (0,0), pady = 0)
  cbuttons.append(tk.Button(tabbar, font = "Consolas 13", text = " X ", width=2, relief = "flat", fg="#f00", bg="#020203", activebackground="#0a0e14", borderwidth=0))
  cbuttons[-1].pack(side = "left", padx = (0,5), pady=0)
  totbutts += 1

totbutts = 0
cbuttons = []
tbuttons = []

root = tk.Tk()

seltab = tk.IntVar()

tabbar = tk.Frame(root, bg = "#020203")
tabbar.pack(fill="x")
newbtn = tk.Button(tabbar, font="Consolas 13 bold", text = "+", command = newtab, width = 2, relief = "flat", bg="#020203", fg="#b3b1ad", activebackground="#020203", borderwidth=0)
newbtn.pack(side="right", padx= 5, pady=0)
codeview = ScrollCode(root, font="Consolas 13", lexer=pygments.lexers.CLexer, color_scheme="ayu-dark")
codeview.pack(fill="both", expand=True)

newtab()

root.after(100, tabupd)
root.mainloop()
