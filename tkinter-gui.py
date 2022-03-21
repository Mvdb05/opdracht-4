from cgitb import text
from multiprocessing.spawn import get_preparation_data
from turtle import color
from pyfiglet import figlet_format
import tkinter as tk
import datetime


# name = input("Whats your name?")
# color = input("What color do you want to use?")


# ascii = figlet_format(text=name, font="standard")

# print(ascii)


window = tk.Tk()

# greeting = tk.Label(
#     text=ascii,
#     width=100,
#     height=30,
#     font='Courier',
#     fg=str(color)
#     )
label = tk.Label(
    text="Vul hier je geboortejaar in: ",
    bg="#DCDCDC",
    width=43
)

entry = tk.Entry(
    width=50,
    bg="#D3D3D3",
    
    )


def LeeftijdBerekenen():
    datum = datetime.datetime.now().year
    geboortejaar = int(entry.get())
    leeftijd = datum - int(geboortejaar)
    leeftijdtext["text"]="je bent " + str(leeftijd) + " jaar oud." 
    
leeftijdtext = tk.Label()    
B = tk.Button(
    window,
    text="Click Me",
    command=LeeftijdBerekenen)
    
    



# greeting.pack()
label.pack()
entry.pack()
leeftijdtext.pack()
B.pack()
window.mainloop()

