import tkinter as tk
from tkinter import ttk

class Pokemon:
    def __init__(self, id, nombre, descripcion, hp, ataque, defensa, tipos):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.tipos = tipos

    def mostrar_info(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nHP: {self.hp}\nAtaque: {self.ataque}\nDefensa: {self.defensa}"

    def get_tipo(self):
        return self.tipos

# Simulación de la base de datos de Pokémon
pokemons_objetos = {
    1: Pokemon(1, "Bulbasaur", "Una semilla extraña fue plantada...", 45, 49, 49, ["planta", "veneno"]),
    2: Pokemon(2, "Ivysaur", "Cuando las semillas crecen...", 60, 62, 63, ["planta", "veneno"]),
    3: Pokemon(3, "Venusaur", "Este Pokémon tiene una flor enorme...", 80, 82, 83, ["planta", "veneno"]),
    4: Pokemon(4, "Charmander", "Un Pokémon de tipo fuego...", 39, 52, 43, ["fuego"]),
    5: Pokemon(5, "Charmeleon", "Este Pokémon se vuelve más feroz...", 58, 64, 58, ["fuego"]),
    6: Pokemon(6, "Charizard", "Este Pokémon puede volar a grandes alturas...", 78, 84, 78, ["fuego", "volador"]),
    # Agregar más Pokémon según sea necesario
}

# Función de búsqueda por tipo
def buscar_tipo(tiponame, pokemon_objetos):
    resultados = []
    lista_nombres = []
    for pokemon in pokemon_objetos.values():
        tipos = pokemon.get_tipo()
        if tiponame in tipos:
            resultados.append(pokemon.mostrar_info())
            lista_nombres.append(pokemon.nombre)
    return resultados, lista_nombres

# Función para manejar la selección del tipo en la interfaz
def mostrar_pokemon_por_tipo():
    tipo_seleccionado = tipo_combobox.get()
    resultados, lista_nombres = buscar_tipo(tipo_seleccionado, pokemons_objetos)
    
    resultado_text.delete(1.0, tk.END)  # Limpiar el área de resultados
    lista_pokemon.delete(0, tk.END)  # Limpiar el Listbox
    
    if resultados:
        resultado_text.insert(tk.END, "\n\n".join(resultados))
        for nombre in lista_nombres:
            lista_pokemon.insert(tk.END, nombre)
    else:
        resultado_text.insert(tk.END, "No se encontraron Pokémon de ese tipo.")

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Búsqueda de Pokémon por Tipo")

# Etiqueta y ComboBox para seleccionar tipo
tipo_label = tk.Label(root, text="Selecciona un tipo de Pokémon:")
tipo_label.pack(pady=10)

tipos = ["planta", "veneno", "fuego", "volador", "agua", "bicho"]  # Añadir más tipos según sea necesario
tipo_combobox = ttk.Combobox(root, values=tipos)
tipo_combobox.pack(pady=10)

# Botón para realizar la búsqueda
buscar_button = tk.Button(root, text="Buscar Pokémon", command=mostrar_pokemon_por_tipo)
buscar_button.pack(pady=10)

# Área de texto para mostrar los resultados
resultado_text = tk.Text(root, width=60, height=10)
resultado_text.pack(pady=10)

# Listbox para mostrar los nombres de los Pokémon
lista_label = tk.Label(root, text="Pokémon encontrados:")
lista_label.pack(pady=10)

lista_pokemon = tk.Listbox(root, width=40, height=10)
lista_pokemon.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
