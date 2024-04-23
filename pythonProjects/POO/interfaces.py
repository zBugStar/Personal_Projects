import tkinter
from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
raiz.geometry("960x540")
raiz.resizable(0,1)
raiz.config(bg="white")

label1 = tkinter.Label(raiz, text="Hola, bienvenido a mi programa", bg="lightblue", fg="beige", font=("Arial", 12))
label1.place(x=150, y=100)


def saludo():
    tkinter.Label(raiz, text="Hola, bienvenido a mi programa", bg="lightblue", fg="beige", font=("Arial", 12), )


def salir():
    raiz.destroy()


button = tkinter.Button(raiz, text="Salir", height=5, width=10, command=salir)
button.config(bg="red", fg="white", font=("Arial", 12))
button.winfo_geometry()
button.place(x=250, y=338.9)

button2 = tkinter.Button(raiz, text="Saludo", height=5, width=10, command=saludo,)
button2.config(bg="green", fg="white", font=("Courier", 12))
button2.place(x=250, y=100,)

raiz.mainloop()

label1.pack()
button.pack()
button2.pack()
