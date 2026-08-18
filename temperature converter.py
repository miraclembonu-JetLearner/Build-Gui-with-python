from tkinter import*

root = Tk()

root.title("Temperature Converter (celsius to fahrenheit)")

root.geometry("400x500")

Temperature_change = Label(root, text="celsius to fahrenheit", font=("Arial", 20)).place(x=130, y=20)

Temperature_entry = Label(root, text="Enter temperature in celsius").place(x=130, y=60)
Temperature_entry = Entry(root,width=25).place(x=130, y=90)

convert_button = Button(root, text="Convert", background="lightgray").place(x=130, y=120)
converted_temperature = Label(root, width=25).place(x=130, y=150)


mainloop()