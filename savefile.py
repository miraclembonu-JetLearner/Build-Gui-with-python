from tkinter import*
from tkinter.ttk import*

from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry("200x100")


def saves():
    file = [("All files","*."),("Text documents","*.txt")]
    Files = asksaveasfile (filetypes = file, defaultextension = file)
   

btn = Button(root, text="Save file", command= lambda:saves())
btn.pack(side=TOP , pady=20)


mainloop()