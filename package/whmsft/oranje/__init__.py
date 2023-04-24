import tkinter as tk
from tkinter import ttk
from pygments import lexers
from chlorophyll import CodeView

editor = tk.Tk()

ttk.Style().configure("TLineNumbers", background="#202020", foreground="#ffffff")
codeview = CodeView(editor, lexer=lexers.PythonLexer, color_scheme="monokai", font="Cascadia\ Code 14", tab_width=4)
codeview.pack(fill="both", expand=True)
editor.after(10, editor.quit)
if __name__ == "__main__": editor.mainloop()