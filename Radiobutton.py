from tkinter import*
from tkinter import messagebox
root = Tk()

root.title("My favorite dishes")
root.geometry("400x300")

choices = StringVar()

Label(root, text="What is your favorite dish?").place(x=150, y=20)

Radiobutton(root, text="Burger", variable=choices, value="burger").place(x=150, y=50)
Radiobutton(root, text="Pizza", variable=choices, value="pizza").place(x=150, y=80)
Radiobutton(root, text="Pasta", variable=choices, value="pasta").place(x=150, y=110)
Radiobutton(root, text="Chicken Sandwich", variable=choices, value="chicken sandwich").place(x=150, y=140)

def submit():
    messagebox.showinfo("Your favorite dish is"," you selected" + choices.get())

submit_button = Button(root, text="submit", background="lightgray", command=submit) 
submit_button.place(x=150, y=170)

root.mainloop()