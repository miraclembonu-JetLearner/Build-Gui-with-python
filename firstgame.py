from tkinter import *

root  = Tk()
root.title("Rock Paper Scissors Game")


label_tittle = Label(root,text="Rock paper siccors game" ,font=("Times new roman" , 20), fg="brown")
label_tittle.pack()

winner_label = Label(root, text="abc123", font=("times new roman", 20), fg="red")
winner_label.pack()

input_frame = Frame(root)
input_frame.pack()

paper_button = Button(input_frame, text="paper", font=("Times new roman", 16), fg = "blue" , bg = "Gray" , width=15)
paper_button.grid(row=0, column=0, padx=10)

rock_button = Button(input_frame, text="rock", font=("Times new roman", 16), fg = "red" , bg = "Gray" , width=15)
rock_button.grid(row=0, column=1, padx=10)

scissors_button = Button(input_frame, text="scissors", font=("Times new roman", 16), fg = "green" , bg = "Gray" , width=15)
scissors_button.grid(row=0, column=2, padx=10) 

player_choice_label = Label(input_frame, text="player choice: " , font =("Times new roman" , 16) , fg= "black")
player_choice_label.grid(row=1, column=0, columnspan=5 ,pady=10)

computer_choice_label = Label(input_frame, text="computer choice: " , font =("Times new roman" , 16) , fg= "black")
computer_choice_label.grid(row=2, column=0, columnspan=5 ,pady=10)


root.mainloop()