from tkinter import *


#Paleta de colores para los botones
fondo = "#0d1b2a"
botonNumeros = "#778da9"
botonNumerosHover = "#003049"
botonOperaciones = "#c1121f"
botonOperacionesHover = "#780000"
texto = "black"
textoOperaciones = "White"

#Creamos la ventana y ponemos sus caracteristicas
window = Tk()
window.title("Calculadora")
window.config(bg = fondo)



i=0

entryText = Entry(window, font = "Calibri 20")
entryText.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 2.5)

def click_boton(valor):
    global i 
    entryText.insert(i,valor)
    if valor == "**":
        i+=2
    else:
        i+=1
    
def borrar():
    entryText.delete(0, END)
    i = 0
    
def hacer_operacion():
    ecuacion = entryText.get()
    resultado = eval(ecuacion)
    entryText.delete(0,END)
    entryText.insert(0, resultado)
    i=0

#Funcion para cambiar el background cuando pase el puntero
def on_enterNum(event):
    event.widget.config(bg = botonNumerosHover)

def on_leaveNum(event):
    event.widget.config(bg = botonNumeros)
    
def on_enterOP(event):
    event.widget.config(bg = botonOperacionesHover)

def on_leaveOP(event):
    event.widget.config(bg = botonOperaciones)
    
#Estilos para lso botonoes
estilosNumeros = {'fg':texto, 'font': ('Calibri', 12), 'bg': botonNumeros,  }
estilosOperaciones = {'fg':textoOperaciones, 'font': ('Calibri', 12), 'bg': botonOperaciones}
    
#Botones
boton1 = Button(window, text="1", widt=5,height=2, command = lambda: click_boton(1), **estilosNumeros)
boton2 = Button(window, text="2", widt=5,height=2, command = lambda: click_boton(2), **estilosNumeros)
boton3 = Button(window, text="3", widt=5,height=2, command = lambda: click_boton(3), **estilosNumeros)
boton4 = Button(window, text="4", widt=5,height=2, command = lambda: click_boton(4), **estilosNumeros)
boton5 = Button(window, text="5", widt=5,height=2, command = lambda: click_boton(5), **estilosNumeros)
boton6 = Button(window, text="6", widt=5,height=2, command = lambda: click_boton(6), **estilosNumeros)
boton7 = Button(window, text="7", widt=5,height=2, command = lambda: click_boton(7), **estilosNumeros)
boton8 = Button(window, text="8", widt=5,height=2, command = lambda: click_boton(8), **estilosNumeros)
boton9 = Button(window, text="9", widt=5,height=2, command = lambda: click_boton(9), **estilosNumeros)
boton0 = Button(window, text="0", widt=5,height=2, command = lambda: click_boton(0), **estilosNumeros)

boton_borrar = Button(window, text="AC", width=5, height=2, command = lambda: borrar(), **estilosOperaciones)
boton_abrir_parentesis = Button(window, text= "(", width=5, height=2, command = lambda: click_boton("("), **estilosOperaciones)
boton_cerrar_parentesis = Button(window, text= ")", width=5, height=2, command = lambda: click_boton(")"), **estilosOperaciones)
boton_punto = Button(window, text = ".", width=5, height=2, command = lambda: click_boton("."), **estilosOperaciones) 

boton_suma = Button(window, text= "+", width=5, height=2, command = lambda: click_boton("+"), **estilosOperaciones)
boton_resta = Button(window, text= "-", width=5, height=2, command = lambda: click_boton("-"), **estilosOperaciones)
boton_multiplicacion = Button(window, text= "*", width=5, height=2,command = lambda: click_boton("*"), **estilosOperaciones)
boton_division = Button(window, text= "/", width=5, height=2,command = lambda: click_boton("/"), **estilosOperaciones)
boton_pot = Button(window, text="^" , width=5, height = 2, command = lambda: click_boton("**"), **estilosOperaciones)
boton_igual = Button(window, text= "=", width=5, height=2, command = lambda: hacer_operacion(), **estilosOperaciones)

botonesNumeros = (boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton0)
botonesOperaciones = (boton_borrar, boton_abrir_parentesis, boton_cerrar_parentesis, boton_punto,boton_suma,boton_resta,
                      boton_multiplicacion,boton_division,boton_igual)
# ponemos los botones en pantalla 

boton_borrar.grid(row = 1, column=0, padx=2, pady=5, sticky=(N + W + E + S))
boton_abrir_parentesis.grid(row = 1, column=1, padx=2, pady=5, sticky=(N + W + E + S))
boton_cerrar_parentesis.grid(row = 1, column=2, padx=2, pady=5, sticky=(N + W + E + S))
boton_division.grid(row = 1, column=3, padx=2, pady=5, sticky=(N + W + E + S))

boton9.grid(row=2,column = 0, padx=2,pady=5, sticky=(N + W + E + S))
boton8.grid(row=2,column = 1, padx=2,pady=5, sticky=(N + W + E + S))
boton7.grid(row=2,column = 2, padx=2,pady=5, sticky=(N + W + E + S))
boton_multiplicacion.grid(row=2,column = 3, padx=2,pady=5, sticky=(N + W + E + S))

boton6.grid(row=3,column = 0, padx=2,pady=5, sticky=(N + W + E + S))
boton5.grid(row=3,column = 1, padx=2,pady=5, sticky=(N + W + E + S))
boton4.grid(row=3,column = 2, padx=2,pady=5, sticky=(N + W + E + S))
boton_suma.grid(row=3,column = 3, padx=2,pady=5, sticky=(N + W + E + S))

boton1.grid(row=4,column = 0, padx=2,pady=5, sticky=(N + W + E + S))
boton2.grid(row=4,column = 1, padx=2,pady=5, sticky=(N + W + E + S))
boton3.grid(row=4,column = 2, padx=2,pady=5, sticky=(N + W + E + S))
boton_resta.grid(row=4,column = 3, padx=2,pady=5, sticky=(N + W + E + S))

boton0.grid(row=5,column = 1, padx=2,pady=5, sticky=(N + W + E + S))
boton_punto.grid(row= 5, column = 2, padx=2, pady=5, sticky=(N + W + E + S))
boton_igual.grid(row=5,column = 3, padx=2, pady=5, sticky=(N + W + E + S))
boton_pot.grid(row=5, column = 0, padx=2, pady = 5, sticky=(N + W + E + S))

for boton in botonesNumeros:
    
    boton = window.nametowidget(boton)
    boton.bind('<Enter>', on_enterNum)
    boton.bind('<Leave>', on_leaveNum)
    
for boton in botonesOperaciones:
    
    boton = window.nametowidget(boton)
    boton.bind('<Enter>', on_enterOP)
    boton.bind('<Leave>', on_leaveOP)

window.mainloop()