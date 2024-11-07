import tkinter as tk
from tkinter.ttk import Combobox
from funciones_objetos import *


###FUNCIONAL

ventana = tk.Tk()
ventana.geometry("380x1920")

# Opciones de los tipos de Pokémon de la primera generación
opciones = [
    "normal",
    "fighting",
    "flying",
    "poison",
    "ground",
    "rock",
    "bug",
    "ghost",
    "fire",
    "water",
    "grass",
    "electric",
    "psychic",
    "ice",
    "dragon"
]

# Combobox para seleccionar el tipo
combobox = Combobox(ventana, values=opciones)
combobox.set("Selecciona un tipo")
combobox.pack()

# Lista para mostrar los Pokémon
lista = tk.Listbox(ventana)
lista.pack()

# Función para actualizar la lista de Pokémon en base al tipo seleccionado
def actualizar_lista(event):
    # Limpiar el Listbox antes de insertar los nuevos elementos
    lista.delete(0, tk.END)

    # Obtener el tipo seleccionado
    tipo_seleccionado = combobox.get()
    
    # SE MUESTRA EN LA TERMINAL
    print(f"Tipo seleccionado: {tipo_seleccionado}")  # Verifica que se recibe correctamente el tipo
    
    # Verifica que la función de búsqueda retorne una lista
    normales = Funciones.buscar_pokemon_tipo(str(tipo_seleccionado))

    if normales:  # Si la lista no está vacía
        # Insertar los nombres de los Pokémon en el Listbox
        for pokemon in normales:
            lista.insert(tk.END, pokemon)
    else:
        lista.insert(tk.END, "No se encontraron Pokémon de este tipo.")

# Vincular el evento de cambio de selección en el Combobox con la función de actualización
combobox.bind("<<ComboboxSelected>>", actualizar_lista)



label = tk.Label(ventana,text="escribe el nombre o el numero de pokemon")
label.pack()


def enviar():
    try:
        numero = int(entry.get())
        Funciones.buscar_pokemon(numero)
        
    except:
        Funciones.buscar_pokemon(entry.get())


entry = tk.Entry(ventana)
entry.pack()
button = tk.Button(ventana,text="buscar",command=enviar)
button.pack()

# REVISA LA TERMINAL


ventana.mainloop()


