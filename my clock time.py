from tkinter import*
from tkinter.ttk import*
from time import strftime

root =Tk()
root.title("clock")


#defining the time function
def time():
    string = strftime("%H:%M:%S:%p")
    label.config(text=string)
    label.after(1000,time) #1000 = 1 second

#desgining the clock
label = Label(root, font=("arial", 45, "bold"), background="black", foreground="purple")
label.pack()

time()
mainloop()