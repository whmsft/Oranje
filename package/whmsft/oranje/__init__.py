import tkinter as tk
from tkinter import ttk
from pygments import lexers
from chlorophyll import CodeView

GLOBAL = {}

editor = tk.Tk()

ttk.Style().configure("TLineNumbers", background="#202020", foreground="#ffffff")
codeview = CodeView(editor, lexer=lexers.PythonLexer, color_scheme="monokai", font="Cascadia\ Code 14", tab_width=4)
codeview.pack(fill="both", expand=True)

if __name__ == "__main__": editor.mainloop()
