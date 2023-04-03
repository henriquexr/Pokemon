class Pokemon():
    def __init__(self,especie,tipo,hp,atq,dfs):
        self._especie = especie
        self._tipo = tipo
        self._hp = hp
        self._atq = atq
        self._dfs = dfs
        
    '''def checarVantagen(self,pokemonRival):
        if self._tipo == "normal":
            if pokemonRival._tipo == "fogo":
                pokemonRival._defesa = 1
            elif pokemonRival._tipo == "Grama":
                pokemonRival._defesa = 1
            elif pokemonRival._tipo == "Agua":
                pokemonRival._defesa = 1
            else:
                pokemonRival._defesa = 1
        return pokemonRival._defesa'''


class Grama(Pokemon):
    def __init__(self, especie, tipo, hp, ataque, defesa):
        super().__init__(especie, tipo, hp, ataque, defesa)
        self._tipo = "Grama"
        self._movimento = "Chicote de cipó"

    '''def checarVantagen(self,pokemonRival):
        if self._tipo == "Grama":
            if pokemonRival._tipo == "fogo":
                pokemonRival._defesa = 0,5
            elif pokemonRival._tipo == "Grama":
                pokemonRival._defesa = 1
            elif pokemonRival._tipo == "Agua":
                pokemonRival._defesa = 2
            else:
                pokemonRival._defesa = 2'''
        


class Fogo(Pokemon):
    def __init__(self, especie, tipo, hp, ataque, defesa):
        super().__init__(especie, tipo, hp, ataque, defesa)
        self._tipo = "Fogo"
        self._movimento = "Chamas"

    '''def checarVantagen(self,pokemonRival):
        if self._tipo == "Fogo":
            if pokemonRival._tipo == "fogo":
                pokemonRival._defesa = 1
            elif pokemonRival._tipo == "Grama":
                pokemonRival._defesa = 2
            elif pokemonRival._tipo == "Agua":
                pokemonRival._defesa = 0.5
            else:
                pokemonRival._defesa = 2'''


class Agua(Pokemon):
    def __init__(self, especie, tipo, hp, ataque, defesa):
        super().__init__(especie, tipo, hp, ataque, defesa)
        self._tipo = "Agua"
        self._movimento = "Bolhas"

    '''def checarVantagen(self,pokemonRival):
       if self._tipo == "Agua":
            if pokemonRival._tipo == "fogo":
                pokemonRival._defesa = 2
            elif pokemonRival._tipo == "Grama":
                pokemonRival._defesa = 0,5
            elif pokemonRival._tipo == "Agua":
                pokemonRival._defesa = 1
            else:
                pokemonRival._defesa = 2'''

