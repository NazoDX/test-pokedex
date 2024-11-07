from instancias_pokemon import *
"""
de el archivo instancias pokemon que sera
automatico a la hora del uso del programa 
se importa todo lo que se ha hecho
"""

class Funciones():

    """
    Creamos una clase llamada Funciones
    esta en especial se limita a unicamente 
    los tipos de busqueda en la pokedex
    """

    # almacenamos en una variable los objetos para mas comodidad
    dicpokemon = Pokemon.pokemons_objetos
    # Pokemon.pokemons_objetos <--- almacena un diccionario con objetos

    @classmethod
    def buscar_pokemon(cls, num_o_nombre):
        """
        Esta clase estatica toma tomara un argumento cual puede ser numero
        o bien puede ser texto para buscar la informacion del pokemon

        num_o_nombre <---- es el argumento  
        """

        # recorre bucle el diccionario de objetos
        for id, pokemon in cls.dicpokemon.items():

            encontrado = False  # esta variable sirve para controlar si se ha encontrado
            # por default sera false

            # ahora verifica si es elargumento es igual al nombre del pokemon
            # o sino el numero que se pone en el argumento es igualal id
            # lo es termina el bucle
            if num_o_nombre == pokemon.get_nombre() or num_o_nombre == id:
                encontrado = True
                print("Se encontro el pokemon")
                print(pokemon)
                break

        # si no se entra a la condicional entonces imprime esto
        if not encontrado:
            print("No se encuentra el pokemon")         
    
    @classmethod
    def buscar_pokemon_tipo(cls, tipo):
        """ 
        Esta clase se encarga de la busqueda de pokemon por tipo
        donde retorna en forma de lista los pokemones que son x 
        tipo
        """
        lista_tipos = []
        
        # recorrer el diccionario de objetos
        for id, pokemon in cls.dicpokemon.items():
            
            # por cada pokemon tomar el tipo
            tipos = pokemon.get_tipo()
            # luego reccorre el contendio se tipos
            for contenido in tipos:
                # si el nombre del tipo de pokemon coincide con el argumento tipo
                if contenido == tipo:
                    #imprime la informacion en consola 
                    print(f"{id}, pokemon: {pokemon.get_nombre()},{pokemon.get_tipo()}")
                    # y agrega el nombre del pokemon en una lista para retornarla 
                    lista_tipos.append(pokemon.get_nombre())
                    
        return lista_tipos
# ve probando uno a uno y si vez que dice en terminal pokemon creado como objeto
# recuerda que estamos imprtando toda la funcionalidad automatica de instancias_pokemon
# buscar pokemon por numero o nombre
Funciones.buscar_pokemon(12)          
Funciones.buscar_pokemon(0)   #<--- no existe el pokemon 0       
Funciones.buscar_pokemon("metapod") 

# nos devuelve una lista de pokemons tipo x si se imprime lo veras
# si solo pones Funciones.buscar_pokemon("tipo") se mostrara en terminal
# los pokemons de ese tipo
print(Funciones.buscar_pokemon_tipo("electric")) 
print(Funciones.buscar_pokemon_tipo("fire"))
