
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Flight Booker")
window.geometry("350x300")

tk.Label(window, text="Destination").pack()

destination = ttk.Combobox(window, values=["Paris", "New York", "Tokyo"])
destination.pack()

tk.Label(window, text="Class").pack()

flight_class = tk.StringVar(value="Economy")

tk.Radiobutton(window, text="Economy", variable=flight_class, value="Economy").pack()
tk.Radiobutton(window, text="Business", variable=flight_class, value="Business").pack()
tk.Radiobutton(window, text="First Class", variable=flight_class, value="First Class").pack()

def calculate():
    prices = {"Paris": 500, "New York": 700, "Tokyo": 900}
    extras = {"Economy": 0, "Business": 200, "First Class": 500}

    place = destination.get()

    if place == "":
        result.config(text="Select a destination")
    else:
        total = prices[place] + extras[flight_class.get()]
        result.config(text="Total Ticket Price: £" + str(total))

tk.Button(window, text="Calculate Price", command=calculate).pack(pady=15)

result = tk.Label(window, text="Total Ticket Price: £0")
result.pack()

window.mainloop()
