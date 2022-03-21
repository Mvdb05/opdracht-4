from cgitb import text
import tkinter as tk
import datetime

def LeeftijdBerekenen():

    window = tk.Tk()

    label = tk.Label(
        text="Voer hier uw geboortejaar in: ",
        fg="Black",
    )

    entry = tk.Entry()

    button = tk.Button(
        text="Submit",
        fg="Black"
        
    )
    
    label.pack()
    entry.pack()
    button.pack()


    geboortejaar = entry.get()
    datum = datetime.datetime.now().year
    leeftijd = datum - int(float(geboortejaar))

    greeting = tk.Label(
        text=leeftijd
        
    )

    greeting.pack()
    window.mainloop()

LeeftijdBerekenen()