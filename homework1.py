from tkinter import*

root = Tk()

root.geometry("200x300")
root.config(background="lightblue")

root.title("cinema booking system")

ticket_number = Label(root, text="How many tickets would you like?").place(x=70,y=100)

tickets_spinner = Spinbox(root, from_=0, to=5).place(x=100, y=140)

book_now = Button(root,text ="Book now", background="red").place(x=120,y=180)


root.mainloop()