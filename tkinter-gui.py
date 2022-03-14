from multiprocessing.spawn import get_preparation_data
from turtle import color
from pyfiglet import figlet_format
import tkinter as tk


name = input("Whats your name?")
color = input("What color do you want to use?")

ascii = figlet_format(text=name, font="doh")

print(ascii)


window = tk.Tk()


greeting = tk.Label(
    text=ascii,
    width=100,
    height=30,
    font='Courier',
    fg=str(color)
    )

greeting.pack()
window.mainloop()
