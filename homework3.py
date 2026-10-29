from tkinter import*
import random
import math
import tkinter.messagebox

root = Tk()
root.title("Math Whiz")
root.geometry("400x400")

num1 = random.randint(1,10)

num2 = random.randint(1,10)



def correct():
    tkinter.messagebox.showinfo("Correct!", "You are a Math Whiz")

def wrong():
    tkinter.messagebox.showinfo(f"Wrong!", f"The answer was {answer}")

def check_answer():
    user_answer = answer_entrybox.get()
    if user_answer.isdigit():
        if int(user_answer) == answer:
            correct()
        else:
            wrong()
    else:
        tkinter.messagebox.showinfo("Error", "Please enter a valid number.")

answer = num1 * num2

num1_label = Label(root, text=f"Number 1: {num1}")
num1_label.place(x=20, y=60)

num2_label = Label(root, text=f"Number 2: {num2}")
num2_label.place(x=20, y=80)

answer_btn = Button(root, text=(f"Enter your answer!"), command=check_answer)
answer_btn.place(x=20, y=120)



answer_entrybox = Entry(root,text="")
answer_entrybox.place(x=20, y=160)

root.mainloop()