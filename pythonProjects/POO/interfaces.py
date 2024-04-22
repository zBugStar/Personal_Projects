import tkinter
from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1, 1)
raiz.geometry("500x500")
raiz.resizable(0, 0)
raiz.config(bg="white")

label1 = tkinter.Label(raiz, text="Hola, bienvenido a mi programa", bg="lightblue", fg="beige", font=("Arial", 12))
label1.place(x=100, y=100)

def saludo():
    tkinter.Label(raiz, text="Hola, bienvenido a mi programa", bg="lightblue", fg="beige", font=("Arial", 12)).pack()


def salir():
    raiz.destroy()


button = tkinter.Button(raiz, text="Salir", command=salir)
button.config(bg="red", fg="white", font=("Arial", 12))
button.place(x=250, y=250)

button2 = tkinter.Button(raiz, text="Saludo", command=saludo)
button2.config(bg="green", fg="white", font=("Arial", 12))
button2.place(x=250, y=100, width=100, height=50)


raiz.mainloop()

label1.pack()
button.pack()
button2.pack()
