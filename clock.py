from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("500x220")
root.configure(bg="black")


def update_clock():
    current_time = strftime("%H:%M:%S")
    current_day = strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_day)

    root.after(1000, update_clock)


time_label = Label(
    root,
    font=("Verdana", 46, "bold"),
    background="black",
    foreground="purple"
)
time_label.pack(pady=(30, 5))

date_label = Label(
    root,
    font=("Verdana", 18),
    background="black",
    foreground="white"
)
date_label.pack()

update_clock()
root.mainloop()