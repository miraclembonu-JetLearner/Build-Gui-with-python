from tkinter import*
from tkinter.ttk import*

root = Tk()

menubar = Menu(root)

file = Menu(menubar, tearoff=0) #New text file, save, share, exit

menubar.add_cascade(label="File", menu=file)

file.add_command(label="New text file",command =None)
file.add_command(label="Save" , command=None)  
file.add_command(label="Share", command=None)
file.add_command(label="Exit", command=root.destroy)

edit = Menu(menubar, tearoff=0) #cut, copy, paste

menubar.add_cascade(label="Edit", menu=edit)

edit.add_command(label = "Cut", command=None)
edit.add_command(label = "Copy", command=None)
edit.add_command(label = "Paste", command=None)

Go = Menu(menubar, tearoff=0) #Go to home, go to menu, go to order

menubar.add_cascade(label="Go", menu=Go)

Go.add_command(label = "Go to home", command=None)
Go.add_command(label = "Go to menu", command=None)
Go.add_command(label = "Go to order", command=None)

root.config(menu=menubar)
mainloop()

