# clase hecha para crear a cada pokemon a objeto 
# del diccionario pokemon gen 1

from dicc_pokemon import pokemons
"""
primero se ha importado la variable "pokemons"
esta variable contiene un diccionario lleno de los 150 
pokemons de la gen 1
"""
"""
Ejemplo de como se estructura:

pokemons = {
    'bulbasaur': {
        'descripcion': 'Una rara semilla le fue plantada en el lomo al nacer.\
\nLa planta brota y crece con este Pokémon.',
        'tipo': {'poison', 'grass'},
        'peso': 69,
        'altura': 7,
        'habilidad': {'chlorophyll', 'overgrow'},
        'stats': {
            'hp': 45,
            'attack': 49,
            'defense': 49,
            'special-attack': 65,
            'special-defense': 65,
            'speed': 45,
        }
    }
"""


class Pokemon:
    def __init__(self, nombre, descripcion, tipo, peso, altura, habilidad, stats):
        self._nombre = nombre
        self._descripcion = descripcion
        self._tipo = tipo
        self._peso = peso
        self._altura = altura
        self._habilidad = habilidad
        self._stats = stats
    """
    se ha creado una clase llamada Pokemon esta misma 
    tendra todos los atributos necesarios para 
    usarlos como objetos.    
    """
    # Getters para cada atributo
    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def get_tipo(self):
        return self._tipo

    def get_peso(self):
        return self._peso

    def get_altura(self):
        return self._altura

    def get_habilidad(self):
        return self._habilidad

    # Getters específicos para cada estadística en `stats`
    def get_hp(self):
        return self._stats.get("hp")

    def get_attack(self):
        return self._stats.get("attack")

    def get_defense(self):
        return self._stats.get("defense")

    def get_special_attack(self):
        return self._stats.get("special-attack")

    def get_special_defense(self):
        return self._stats.get("special-defense")

    def get_speed(self):
        return self._stats.get("speed")

    # Método para mostrar información general con solo imprimir el objeto
    # con solo hacer print(objeto) mostrara en la terminal como se estructura 
    def __str__(self):
        # a primeras pensaras que desorden pero es como se mostrara en la terminal
        info = f"""
Nombre: {self.get_nombre()},
Descripcion: {self.get_descripcion()}
Tipo: {self.get_tipo()},
Peso: {self.get_peso()} kg,
Altura: {self.get_altura()} m,
Hablidades: {self.get_habilidad()},
Stats:
    Hp: {self.get_hp()}     
    Ataque: {self.get_attack()}     
    Defensa: {self.get_defense()}     
    Ataque Especial: {self.get_special_attack()}     
    Defensa Especial: {self.get_special_defense()}  
    Velocidad: {self.get_speed()}"""
        return info
    
    
    """
    una vez hecha la plantilla se hara una variable 
    que nos servira como diccionario de objeos 
    funcionando similar solo que aqui el id (numero de pokemon)
    sera la key para acceder al objeto en este caso al pokemon
    """
    # diccionario pokemon(objetos)
    pokemons_objetos = {}
    # variable para el id 
    # nota que en el diccionario ya estan ordenados 
    # por lo que no habra problema 
    numero = 0
    
    @classmethod
    def inicializar_objetos(cls):
        
        """
        en este metodo de clase lo que se usara son 
        las variables ya hechas
        
        se hace un bucle que recorre cada pokemon
        donde en el diccionario para acceder a todo 
        llave principal es el nombre.
        luego por cada nombre accedido se suma +1 al contador que nos
        funciona para id 
        creando la estructura similar:
        
        cls.pokemons_objetos[cls.numero] = Pokemon(
                nombre=nombre,
                descripcion=datos['descripcion'],
                tipo=datos['tipo'],
                peso=datos['peso'],
                altura=datos['altura'],
                habilidad=datos['habilidad'],
                stats=datos['stats']
                )
        """
        
        for nombre, datos in pokemons.items():
            cls.numero += 1
            cls.pokemons_objetos[cls.numero] = Pokemon(
                nombre=nombre,
                descripcion=datos['descripcion'],
                tipo=datos['tipo'],
                peso=datos['peso'],
                altura=datos['altura'],
                habilidad=datos['habilidad'],
                stats=datos['stats']
                )
            print(f"Pokemon No{cls.numero} creado como objeto")
            
        #print(f"Numero total de pokemons en la pokedex {cls.numero}")
        # si quieres ver si todos los objetos se instanciaron
            
    """
    Este metodo de clase funciona unicamente para 
    verificar el contenido del objeto en forma de str
    
    por cada pokemon en pokemon_objetos
    mostrara su id(key) y su llamada del objeto en str
    """
    @classmethod
    def mostrar_objetos(cls):
        for id, pokemon in cls.pokemons_objetos.items():
            print(f"ID: {id}{pokemon}\n")
            
            
# Inicializar todos los Pokémon esto si o si debe de hacerse
Pokemon.inicializar_objetos()


# usarlo para ver como se estructura en el diccionario de objetos (opcional)
# puedes probarlo
#Pokemon.mostrar_objetos()

# podemos acceder a los objetos usando la variable;
#pokemons_objetos
# es una diccionario que contiene todos los objetos
# USO POR MODULARIDAD:
# Pokemon.pokemons_objetos <----- se puede usar para almacenar o no

    