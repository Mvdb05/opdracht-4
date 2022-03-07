from turtle import color
from pyfiglet import figlet_format
import tkinter as tk
from unicodedata import name
window = tk.Tk()


ascii = figlet_format("Max", font="standard")

greeting = tk.Label(
    text=ascii,
    width=30,
    height=10
    )
greeting.pack()

label = tk.Label(
    text="Vul hier je naam in:",
    bg="#DCDCDC",
    width=43
)

entry = tk.Entry(
    width=50,
    bg="#D3D3D3",
    
    )
name = entry.get()


label.pack()
entry.pack()
window.mainloop()