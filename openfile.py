from tkinter import*
from tkinter.ttk import*

from tkinter.filedialog import askopenfile

root = Tk()
root.geometry("200x100")

def openfile():
    file = askopenfile(mode="r", filetypes=[("python files" ,'*.py')])
    if file is not None :
        content = file.read()
        print(content)

btn = Button(root, text="open files", command= lambda:openfile())
btn.pack(side=TOP , pady=10)

mainloop()