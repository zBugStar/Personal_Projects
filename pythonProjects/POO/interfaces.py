import tkinter
from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1,1)
raiz.geometry("650x350")
raiz.resizable(0,0)
raiz.config(bg="white")

def saludo():
    tkinter.Label(raiz, text="Hola, bienvenido a mi programa", bg="lightblue", fg="beige", font=("Arial", 12)).pack()
def salir():
    raiz.destroy()


button = tkinter.Button(raiz, text="Salir", command=salir)
button.config(bg="red", fg="white", font=("Arial", 12))

button2 = tkinter.Button(raiz, text="Saludo", command=saludo)
button.config(bg="green", fg="white", font=("Arial", 12))

button.pack()
button2.pack()


raiz.mainloop()



