# Import required packages
from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()
master.title("Digital clock")

def get_time():
    # Format time HH:MM:SS AM/PM
    time_val = time.strftime("%H:%M:%S %p")
    clock.config(text=time_val)
    clock.after(200, get_time)

clock = Label(master, font=("Arial", 60), bg="black", fg="purple")
clock.pack()

# Call function to get current time
get_time()

# Keep the display of time running until closed
master.mainloop()