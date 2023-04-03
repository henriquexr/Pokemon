class Pokemon():
    def __init__(self,especie,tipo,hp):
        self._especie = especie
        self._tipo = tipo
        self._hp = hp

class Grama(Pokemon):
    def __init__(self, especie, tipo, hp):
        super().__init__(especie, tipo, hp)
        self._tipo = "Grama"
        



class Fogo(Pokemon):
    def __init__(self, especie, tipo, hp):
        super().__init__(especie, tipo, hp)
        self._tipo = "Fogo"



class Agua(Pokemon):
    def __init__(self, especie, tipo, hp):
        super().__init__(especie, tipo, hp)
        self._tipo = "Agua"
