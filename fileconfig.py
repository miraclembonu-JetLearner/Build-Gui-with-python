from tkinter import*
from tkinter.filedialog import*

#Creates a window
root=Tk()

#Title of the window
root.title("File Dialog")


def open_file():
    fin = askopenfile(title="Open file")

    if fin is not None:
        listbox.delete(0, END)

        items = fin.readlines()
        for item in items:
            listbox.insert(END, item.strip())

def save_file():
    fout = asksaveasfile(title="Save file")

    if fout is not None:
       for item in listbox.get(0, END):
           print(item.strip(), file=fout)

           listbox.delete(0, END)

def addd_item():
    listbox.insert(END, item_entry.get())


    item_entry.delete(0, END)

def delete_item():
    index = listbox.curselection()

    if index:
        listbox.delete(index)

#creates the button- save,open,delete
open_button = Button(root,text="Open", command=open_file, width =15)
delete_button = Button(root,text="Delete", command=delete_item, width=15)
save_button = Button(root,text="Save", command=save_file, width=15)
add_button = Button(root,text="Add", command=addd_item, width=15)

#place the buttonss at difrent directions
open_button.pack(side=LEFT, padx=5, pady=5)
delete_button.pack(side=RIGHT, padx=5, pady=5)
save_button.pack( padx=5, pady=5)
add_button.pack( padx=5, pady=5)

item_entry = Entry(root, width=50)
item_entry.pack(padx=5, pady=5)

#Creates a listbox to display the items
frame = Frame(root)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, width=50, yscrollcommand=scrollbar.set)

for i in range(1, 100):
    listbox.insert(END, "List " + str(i))

listbox.pack(side=LEFT, padx=5)
scrollbar.config(command=listbox.yview)
frame.pack(side=RIGHT)

mainloop()