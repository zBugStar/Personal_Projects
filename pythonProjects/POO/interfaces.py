import tkinter
from tkinter import *

window = Tk()
window.title("Ventana de pruebas")
window.geometry("960x540")
window.resizable(1, 1)
window.config(bg="white")

titlePage = tkinter.Label(window, text="Welcome to Genius Help", font=("Open Sans", 26))
titlePage.place(x=20, y=33)


def exit():
    window.destroy()


exitButton = tkinter.Button(window, text="Exit", height=1, width=4, command=exit, borderwidth=5,)
exitButton.config(bg="red", fg="white", font=("Arial", 12))
exitButton.place(x=850, y=450)


window.mainloop()

