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
        
        self._moviemnto = "Lança chamas"
        self._tipo = "Fogo"

class Agua(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = "Jato d'água"
        self._tipo = "Grama"

class Grama(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

        self._movimento = ""

class Eletrico(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

class Psiquico(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

class Fada(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)

class Metal(Pokemon):
    def __init__(self, nome, tipo, especie, ataque, defesa, movimento, hp, level):
        super().__init__(nome, tipo, especie, ataque, defesa, movimento, hp, level)




