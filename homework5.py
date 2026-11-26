from tkinter import *

def add_guest():
    name = entry.get()
    if name != "":
        guest_list.insert(END, name)
        entry.delete(0, END)

def remove_guest():
    selected = guest_list.curselection()
    if selected:
        guest_list.delete(selected)

window = Tk()
window.title("Party Planner")
window.geometry("300x300")

entry = Entry(window, width=25)
entry.pack(pady=10)

add_button = Button(window, text="Add Guest", command=add_guest)
add_button.pack()

guest_list = Listbox(window, width=30, height=10)
guest_list.pack(pady=10)

remove_button = Button(window, text="Remove Selected", command=remove_guest)
remove_button.pack()

window.mainloop()