from tkinter import *
root = Tk()

root.geometry("400x500")
root.config(background="lightblue")

username = Label(root, text="username").place(x=50, y=60)
username_entry = Entry(root,width=25).place(x=130, y=60)

password = Label(root, text="Password").place(x=50, y=100)
password_entry = Entry(root,show="*",width=25).place(x=130, y=100)

food = Label(root, text="what food do you like: chicken sandwich , pizza, pasta ? or None").place(x=50, y=140)
food_entry = Entry(root,width=25).place(x=130, y=170)
food_spinner = Spinbox(root, from_=0, to=4).place(x=300, y=170)


bevarage = Label(root, text="what bevarage do you like: coffee, tea, juice , water ? or None").place(x=50, y=200)
bevarage_entry = Entry(root,width=25).place(x=130, y=230)
bevarage_spinner = Spinbox(root, from_=0, to=4).place(x=300, y=230)

desert = Label(root, text="what desert do you like: ice cream, cake, pie ? or None").place(x=50, y=260)
desert_entry = Entry(root,width=25).place(x=130, y=290)
desert_spinner = Spinbox(root, from_=0, to=4).place(x=300, y=290)

btn = Button(root, text="submit order", background="lightgray").place(x=100, y=320)

"""sp =  Spinbox(root, from_=0, to=10)
sp.place(x=130, y=180)"""


root.mainloop()