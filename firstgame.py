from tkinter import *
import random

Player_score =0
Computer_score =0
options = [("Rock", 0) , ("Paper", 1) , ("Scissors",2)]

def computer_win():
    global Computer_score , Player_score
    Computer_score += 1
    Computer_score_label.config(text=f"Computer score: {Computer_score}")
    winner_label.config(text="Computer wins!")
    Player_score_label.config(text=f"Player score: {Player_score}")

def player_win():
    global Player_score , Computer_score
    Player_score += 1
    Player_score_label.config(text=f"Player score: {Player_score}")
    winner_label.config(text="Player wins!")
    Computer_score_label.config(text=f"Computer score: {Computer_score}")

def tie():
    winner_label.config(text=f"It's a tie",  fg="orange")

def computer_choice():
    return random.choice(options)

def Player_choice(choice):
    global Computer_score , Player_score
    computer_selection = computer_choice()
    player_choice_label.config(text=f"Player choice: {choice[0].capitalize()}")
    computer_choice_label.config(text=f"Computer choice: {computer_selection[0].capitalize()}")
    if choice[1] == computer_selection[1]:
        tie()
    elif (choice[1] == 0 and computer_selection[1] == 2) or (choice[1] == 1 and computer_selection[1] == 0) or (choice[1] == 2 and computer_selection[1] == 1):
        player_win()
    else:
        computer_win()



root  = Tk()
root.title("Rock Paper Scissors Game")


label_tittle = Label(root,text="Rock paper siccors game" ,font=("Times new roman" , 20), fg="brown")
label_tittle.pack()

winner_label = Label(root, text="abc123", font=("times new roman", 20), fg="red")
winner_label.pack()

input_frame = Frame(root)
input_frame.pack()

paper_button = Button(input_frame, text="paper", font=("Times new roman", 16), fg = "blue" , bg = "Gray" , width=15 , command=lambda: Player_choice(options[1]))
paper_button.grid(row=0, column=0, padx=10)

rock_button = Button(input_frame, text="rock", font=("Times new roman", 16), fg = "red" , bg = "Gray" , width=15 , command=lambda: Player_choice(options[0]))
rock_button.grid(row=0, column=1, padx=10)

scissors_button = Button(input_frame, text="scissors", font=("Times new roman", 16), fg = "green" , bg = "Gray" , width=15 , command=lambda: Player_choice(options[2]))
scissors_button.grid(row=0, column=2, padx=10) 

player_choice_label = Label(input_frame, text="player choice: " , font =("Times new roman" , 16) , fg= "black")
player_choice_label.grid(row=1, column=0, columnspan=3 ,pady=10)

computer_choice_label = Label(input_frame, text="computer choice: " , font =("Times new roman" , 16) , fg= "black")
computer_choice_label.grid(row=2, column=0, columnspan=3 ,pady=10)

Computer_score_label = Label(input_frame, text="computer score: ", font=("times new roman", 16), fg= "black")
Computer_score_label.grid(row=3, column=0, columnspan=3 ,pady=10)

Player_score_label = Label(input_frame, text="Player score: ", font=("times new roman", 16), fg= "black")
Player_score_label.grid(row=4, column=0, columnspan=3 ,pady=10)

root.mainloop()
