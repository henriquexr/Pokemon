import random

class Pokemon:
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        self._nome = nome
        self._tipo = tipo
        self._especie = especie
        self._hp = ataque
        self._level = defesa
        self._movimento = movimento
        self._hp = hp
        self._level = level

class Fogo(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, moviemnto, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, moviemnto, hp, level)
        
        self._moviemnto = "Erupção"
        self._tipo = "Fogo"

class Agua(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Bolha saltitante"
        self._tipo = "Agua"

class Grama(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Mega drenagem"
        self._tipo = "Grama"

class Eletrico(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Tensão crescente"
        self._tipo = "Eletrico"

class Psiquico(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Terreno Psíquico"
        self._tipo = "Psiquico"

class Fada(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Cura Floral"
        self._tipo = "Fada"

class Metal(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Bomba magnética"
        self._tipo = "Metal"

class Treinador:
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)
    
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

    def escolherPokemon(self):


