from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Morning Bakery")
root.geometry("460x450")



menubar = Menu(root)

options = Menu(menubar, tearoff=0)

menubar.add_cascade(
    label="Options",
    menu=options
)

options.add_command(
    label="Exit",
    command=root.destroy
)

root.config(menu=menubar)




title = Label(
    root,
    text="Breakfast Menu",
    font=("Arial", 20, "bold")
)

title.pack(pady=25)

donuts_label = Label(
    root,
    text="Donuts ($2):"
)

donuts_label.place(
    x=170,
    y=105
)

donuts = Spinbox(
    root,
    from_=0,
    to=20,
    width=5
)

donuts.set(1)

donuts.place(
    x=258,
    y=103
)

muffins_label = Label(
    root,
    text="Muffins ($3):"
)

muffins_label.place(
    x=170,
    y=145
)

muffins = Spinbox(
    root,
    from_=0,
    to=20,
    width=5
)

muffins.set(3)

muffins.place(
    x=258,
    y=143
)

coffee_label = Label(
    root,
    text="Coffee ($4):"
)

coffee_label.place(
    x=170,
    y=185
)

coffee = Spinbox(
    root,
    from_=0,
    to=20,
    width=5
)

coffee.set(3)

coffee.place(
    x=258,
    y=183
)



order_button = Button(
    root,
    text="Place Order",
    command=None
)

order_button.place(
    x=152,
    y=263,
    width=175,
    height=30
)

mainloop()