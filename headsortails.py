from tkinter import *
import random
root = Tk()

root.title("Coin Toss")
root.geometry("400x300")


# Function to flip coin
def flip_coin():
    result = random.choice(["Heads", "Tails"])

    if result == "Heads":
        result_label.config(text="It's Heads!", fg="blue")
    else:
        result_label.config(text="It's Tails!", fg="blue")


title_label = Label(root,text="Heads or Tails?",font=("Arial", 20))
title_label.pack(pady=30)



Flip_Button = Button(root, text="Flip Coin", font=("Helvetica", 14), command=lambda: flip_coin() , bg="Yellow")
Flip_Button.pack(pady=10)


result_label = Label(root,text="",font=("Arial", 24, "bold"),fg="blue")
result_label.pack(pady=20)

root.mainloop()