import tkinter
from tkinter import *
from tkinter import ttk
import math

# Creamos la ventana de la calculadora
window = Tk()
window.title("Calculadora")
window.geometry("+500+80")

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background="light gray")

# Creamos el frame principal donde va todo el contenido de la calculadora
mainframe = ttk.Frame(window, style="mainframe.TFrame")
mainframe.grid(column=0, row=0)

# Estilos de los labels
style_label1 = ttk.Style()
style_label1.configure("Label1.TLabel", font=("Arial", 14), background="White", anchor="e")

style_label2 = ttk.Style()
style_label2.configure("Label2.TLabel", font=("Arial", 35), background="White", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

# estilos para los botones
style_buttonNumbers = ttk.Style()
style_buttonNumbers.configure("Button.TButton", font=("Arial", 12), background="White", relief="flat")
style_buttonNumbers.map("Button.TButton", foreground=[("active", "blue")], background=[("active", "light gray")])

style_buttonOperations = ttk.Style()
style_buttonOperations.configure("ButtonOP.TButton", font=("Arial", 12), background="#89A9DB", relief="flat")
style_buttonOperations.map("ButtonOP.TButton", foreground=[("active", "white")], background=[("active", "#3747DB")])

style_buttonBorrar = ttk.Style()
style_buttonBorrar.configure("ButtonBorrar.TButton", font=("Arial", 12), background="#DB949A", relief="flat")
style_buttonBorrar.map("ButtonBorrar.TButton", foreground=[("active", "white")],background=[("active", "#DB3747")])

style_buttonRemamnig = ttk.Style()
style_buttonRemamnig.configure("ButtonRemanig.TButton", font=("Arial", 12), background="#89A9DB", relief="flat")
style_buttonRemamnig.map("ButtonRemanig.TButton", foreground=[("active", "white")], background=[("active", "#3747DB")])

# Creamos botones de la calculadora

button0 = ttk.Button(mainframe, text="0", style="Button.TButton")
button1 = ttk.Button(mainframe, text="1", style="Button.TButton")
button2 = ttk.Button(mainframe, text="2", style="Button.TButton")
button3 = ttk.Button(mainframe, text="3", style="Button.TButton")
button4 = ttk.Button(mainframe, text="4", style="Button.TButton")
button5 = ttk.Button(mainframe, text="5", style="Button.TButton")
button6 = ttk.Button(mainframe, text="6", style="Button.TButton")
button7 = ttk.Button(mainframe, text="7", style="Button.TButton")
button8 = ttk.Button(mainframe, text="8", style="Button.TButton")
button9 = ttk.Button(mainframe, text="9", style="Button.TButton")

button_borrar = ttk.Button(mainframe, text=chr(9003), style="ButtonBorrar.TButton")
button_borrar_todo = ttk.Button(mainframe, text="C", style="ButtonBorrar.TButton")
button_parentesis1 = ttk.Button(mainframe, text="(", style="ButtonRemanig.TButton")
button_parentesis2 = ttk.Button(mainframe, text=")", style="ButtonRemanig.TButton")
button_punto = ttk.Button(mainframe, text=".", style="Button.TButton")

button_suma = ttk.Button(mainframe, text="+", style="ButtonOP.TButton")
button_resta = ttk.Button(mainframe, text="-", style="ButtonOP.TButton")
button_multiplicacion = ttk.Button(mainframe, text="*", style="ButtonOP.TButton")
button_division = ttk.Button(mainframe, text=chr(247), style="ButtonOP.TButton")
button_raiz = ttk.Button(mainframe, text=chr(8730), style="ButtonOP.TButton")

button_igual = ttk.Button(mainframe, text="=", style="ButtonOP.TButton")

# Colocamos los botones en la pantalla
button_parentesis1.grid(column=0, row=3)
button_parentesis2.grid(column=1, row=3)
button_borrar_todo.grid(column=2, row=3)
button_borrar.grid(column=3, row=3)

button7.grid(column=0, row=4)
button8.grid(column=1, row=4)
button9.grid(column=2, row=4)
button_division.grid(column=3, row=4)

button4.grid(column=0, row=5)
button5.grid(column=1, row=5)
button6.grid(column=2, row=5)
button_multiplicacion.grid(column=3, row=5)

button1.grid(column=0, row=6)
button2.grid(column=1, row=6)
button3.grid(column=2, row=6)
button_suma.grid(column=3, row=6)

button0.grid(column=0, row=7, columnspan=2, sticky=(W, E))
button_punto.grid(column=2, row=7)
button_resta.grid(column=3, row=7)

button_igual.grid(column=0, row=8, columnspan=3, sticky=(W, E))
button_raiz.grid(column=3, row=8)

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

# Iniciamos la calculadora
window.mainloop()
