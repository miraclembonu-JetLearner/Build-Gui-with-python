from tkinter import*

root = Tk()

root.title("Temperature Converter (celsius to fahrenheit)")

root.geometry("400x500")

def convert():
    Temperature_change = Temperature_entry.get()
    tempfar = (float(Temperature_change)*9/5)+32
    converted_temperature.config(root, text="The temperature change is: "  + str(tempfar) + "°F")


Temperature_change = Label(root, text="celsius to fahrenheit", font=("Arial", 20))  
Temperature_change.place(x=130, y=20)

Temperature_change = Label(root, text="Enter temperature in celsius")    
Temperature_change.place(x=130, y=60)
Temperature_entry = Entry(root,width=25)    
Temperature_entry.place(x=130, y=90)

convert_button = Button(root, text="Convert", background="lightgray" , command = convert)   
convert_button.place(x=130, y=120)
converted_temperature = Label(root, width=25)   
converted_temperature.place(x=130, y=150)


mainloop()