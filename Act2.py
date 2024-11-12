from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

def savefile():
    files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)

root= Tk()
root.geometry("200x100")
btn=Button(root, text="Save", command = lambda : savefile())
btn.pack()
root.mainloop()