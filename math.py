from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("400x300")
root.title("Maths table generator")

title_label = Label(root, text="Maths table")
title_label.grid(row=0, column=0, columnspan = 3, pady=25)

caption = Label(root, text="Number and range:")

caption.grid(row=1, column=0, padx=10)

theNum = IntVar()
numbers = combobox = Combobox(root, textvariable=theNum, width = 5)
numbers.grid(row=1, column=1)

numbers["values"] = tuple(range(101))

endval = IntVar()
r10 = raidio1 = Radiobutton(root, text="10", variable=endval, value=10)
r10.grid(row=1, column=2)

r20 = raidio2 = Radiobutton(root, text="20", variable=endval, value=20)
r20.grid(row=2, column=2, padx=30)

r30 = raidio3 = Radiobutton(root, text="30", variable=endval, value=30)
r30.grid(row=3, column=2, padx=30)


def generate_table():
    tables=""
    for i in range(endval.get()+1):
        tables+=str(theNum.get())+ "    x   "+str(i)+"    =  "+str(theNum.get() *i)+"\n"
    tabel.config(text=tables)

generateButton = Button(root, text="Generate", command=generate_table)
generateButton.grid(row=4, column=1)

tabel = Label(root, text="Table will be generated here")
tabel.grid(row=5, column=1, pady=25)


root.mainloop()