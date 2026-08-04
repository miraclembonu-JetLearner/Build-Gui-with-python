from tkinter import *

root = Tk()

root.geometry("300x400")
root.config(background="lightblue")
color = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]


def change_color():
    import random
    root.config(background=random.choice(color))


# create button #

btn = Button(root, text="click me" ,
              height=2 , width=5 , background= "lightblue", 
              command=change_color
            )

btn.pack(side="top")


root.mainloop()