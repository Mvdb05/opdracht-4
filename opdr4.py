from turtle import color
from pyfiglet import figlet_format
import tkinter as tk
from unicodedata import name
window = tk.Tk()

label = tk.Label(
    text="Vul hier je naam in:",
    bg="#DCDCDC",
    width=43
)

entry = tk.Entry(
    width=50,
    bg="#D3D3D3",
    
    )

button = tk.Button(text="Submit")

name = entry.get()
ascii = figlet_format(text=name, font="doh")

greeting = tk.Label(
    text=ascii,
    width=100,
    height=30,
    font='Courier'
    )

label.pack()
entry.pack()
button.pack()
greeting.pack()
window.mainloop()
print(ascii)