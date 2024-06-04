from tkinter import *

ventana = Tk()
ventana.title("Indice de Masa Corporal")
ventana.config(bg = "#457b9d")


peso_texto = Entry(ventana, font = "Calibri 20")
altura_texto = Entry(ventana, font = "Calibri 20")
resultado_texto = Entry(ventana, font = "Calibri 20")

peso_texto.grid(row = 0, column = 1, columnspan = 4, padx = 5, pady = 5)
altura_texto.grid(row = 1, column = 1, columnspan = 4, padx = 5, pady = 5)
resultado_texto.grid(row = 2, column = 1, columnspan = 4, padx = 5, pady = 5)

def imc():
    peso = float(peso_texto.get())
    altura = float(altura_texto.get())
    resultado = peso/(altura**2)
    resultado_texto.delete(0, END)
    resultado_texto.insert(0, resultado)
    
def reset():
    resultado_texto.delete(0, END)
    altura_texto.delete(0, END)
    peso_texto.delete(0, END)

peso_label = Label(ventana, text = "Peso (Kg)", width = 10, height = 2, bg = "#a8dadc")
altura_label = Label(ventana, text = "Altura (m)", width = 10, height = 2, bg = "#a8dadc")

peso_label.grid(row = 0, column = 0, padx = 5, pady = 5)
altura_label.grid(row = 1, column = 0, padx = 5, pady = 5)

boton_calcular = Button(ventana, text = "Calcular", width = 10, height = 2, command = lambda: imc(), bg = "#e63946")
boton_calcular.grid(row = 2, column = 0, padx = 5, pady = 5) 

boton_reset = Button(ventana, text = "Reset", width = 10, height = 2, command = lambda: reset(), bg = "#e63946")
boton_reset.grid(row = 0, column = 5, padx = 5, pady = 5) 

imc1 = Label(ventana, text ="<18,5 peso bajo", width = 15, height = 2, bg = "#a8dadc")
imc2 = Label(ventana, text = "18,5-24,9 Ideal", width = 15, height = 2, bg = "#a8dadc")
imc3 = Label(ventana, text = "25-29.9 Sobrepeso", width = 15, height = 2, bg = "#a8dadc")
imc4 = Label(ventana, text = "30-34.9 Obesidad", width = 15, height = 2, bg = "#a8dadc")
imc5 = Label(ventana, text = "35-39.9 Obesidad severa", width = 18, height = 2, bg = "#a8dadc")
imc6 = Label(ventana, text = ">40 Obesidad mórbida", width = 18, height = 2, bg = "#a8dadc")

imc1.grid(row = 3, column = 0, padx = 5, pady = 5)
imc2.grid(row = 3, column = 1, padx = 5, pady = 5)
imc3.grid(row = 3, column = 2, padx = 5, pady = 5)
imc4.grid(row = 3, column = 3, padx = 5, pady = 5)
imc5.grid(row = 3, column = 4, padx = 5, pady = 5)
imc6.grid(row = 3, column = 5, padx = 5, pady = 5)

ventana.mainloop()