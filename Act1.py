from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

def open_file():
    file = askopenfile(mode = "r", filetypes = [("Python Files", "*.py")])
    if file is not None:
        content = file.read()
        print(content)
    

root= Tk()
root.geometry("200x100")
btn = Button(root, text="Open", command = lambda:open_file())
btn.pack()

root.mainloop() 