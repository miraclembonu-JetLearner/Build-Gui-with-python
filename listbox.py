from tkinter import*

root = Tk()

root.title("My Favorite Dishes")
root.geometry("400x300")

listbox = Listbox(root, height=8, width=10, font="Arial", activestyle="underline", bg="lightgrey", fg="blue")
listbox.insert(1,"burger")
listbox.insert(2,"pizza")
listbox.insert(3,"pasta")
listbox.insert(4,"chicken sandwich")

listbox.pack()

root.mainloop()