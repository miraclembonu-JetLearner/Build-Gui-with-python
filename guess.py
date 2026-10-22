from tkinter import*
import random
import math 
import tkinter.messagebox
root = Tk()

root.title("welcome to our game")
root.geometry("400x400")

number = random.randint(1, 20)

def send_low():
    tkinter.messagebox.showinfo("Hint", "The number is too low. Try again!")

def send_high():
    tkinter.messagebox.showinfo("Hint", "The number is too high. Try again!")

def check_number():
    guess =  guess_entrybox.get()
    guess = int(guess)
    if guess < number:
        send_low()
    elif guess > number:
        send_high()
    else:
        tkinter.messagebox.showinfo("Congratulations!", "You guessed the number!")

def btn_confirm():
    name = name_entrybox.get()
    tkinter.messagebox.showinfo("name", "well," + name + ",I am thinking of a number between 1 and 20. Can you guess it?")

name_label = Label(root, text="What's your name?").place(x=120, y=0)

Guess_label = Label(root, text="Take a guess").place(x=100, y=40)

ok_btn = Button(root,text="OK", background="white", command=btn_confirm).place(x=250, y=20)

Guess_btn = Button(root,text="Guess", background="white", command=check_number).place(x=250, y=60)

name_entrybox = Entry(root ,text="")
name_entrybox.place(x=120, y=20)

guess_entrybox = Entry(root ,text="")
guess_entrybox.place(x=100, y=60)

root.mainloop()

