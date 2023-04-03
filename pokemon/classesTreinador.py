import random
import classesPokemon
import batalha

#lista q declara os 3 pokemons iniciais
pokemonsIniciais = [
    classesPokemon.Grama("Chikorita","Grama",10),
    classesPokemon.Fogo("Cyndaquil","Fogo",10),
    classesPokemon.Agua("Totodile","Agua",10)
]
#lista que declara os pokemons selvagens
pokemonSelvagen = [
    
    classesPokemon.Agua("Psyduck","Agua",10),
    classesPokemon.Agua("Squirtle","Agua",10),
    classesPokemon.Agua("Poliwag","Agua",10),
    classesPokemon.Fogo("Charmander","Fogo",10),
    classesPokemon.Fogo("Charmander","Fogo",10),
    classesPokemon.Fogo("Charmander","Fogo",10),
    classesPokemon.Grama("Bulbasaurs","Grama",10),
    classesPokemon.Grama("Turtwig","Grama",10),
    classesPokemon.Grama("Odish","Grama",10)

]

class Treinador():
    def __init__(self,nome,pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choices(self._pokemons)
        
class Jogador(Treinador):
    def __init__(self,nome,pokemons):
        super().__init__(nome, pokemons)
#metodo de capturar pokemons
    def capturarPokemons(self,cappok):
        self._pokemons.append(cappok)
        print(f"Voçe capturou um {cappok._especie}")
#metodo que lista os pokemons que o jogador possui
    def MeusPokemons(self):
        for i in range(len(self._pokemons)):
            print(f"{i+1}. {self._pokemons[i]._especie}")
#metodo para escolher o pokemon
    def escolherPokemon(self):
        while True:
            print("Escolha seu pokemon")
            Jogador.MeusPokemons(self)
            pokemonEscolhido = input("Escolha o Pokemon: ")
            if int(pokemonEscolhido) > len(self._pokemons):
                return self._pokemons[(pokemonEscolhido)-1]
            else:
                return self._pokemons[-1]
    
class Rival(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
        self._nome = "Jaen"
    def pokemonRival(self):
        pokemon = random.choice(pokemonsIniciais)
        print(f"{self._nome}, escolheu {pokemon._especie}")
        return pokemon



    

#Inicio do jog
print('''Olá, seja bem vindx ao paraiso pokemon! esses mundo é repleto de criaturas fantasticas e especiais para ficar mais por dentro desse mundo me fale seu nome!''')

nome = input("> ")

print(f"Prazer, {nome}! agora adote um de nossos pokemons disponiveis para lhe acompanhar na sua longa jornada.")
#Chracagem de escolha
while True:
    for i in range(3):
        print(f"{i+1}.{pokemonsIniciais[i]._especie}")
    resp = input("> ")
    primeiroPokemon = pokemonsIniciais[int(resp)-1]

    print(f"Deseja mesmo ficar com {primeiroPokemon._especie}. S|N?")
    opcao = input("> ")

    if opcao == "S":
        break
    else:
        print("Escolha outro Pokemon!")



print(f"O pokemon escolhido foi o {primeiroPokemon._especie}")


jogador = Jogador(nome,[primeiroPokemon])
rival = Rival("Jean", pokemonsIniciais )

while True:
    print('''
    1. Meus Pokemons
    2. Capturar Pokemons
    3. Batalhar
    4. Sair   
''')
    opcao=input(">")
    match (opcao):
        case "1":
            jogador.MeusPokemons()
        case "2":
            pokemon = random.choice(pokemonSelvagen)

            print(f"Deseja capturar {pokemon._especie}?S|N" )

            a = input("> ")

            if a == "S":

                jogador.capturarPokemons(pokemon)
        case "3":
            
            batalha.batalha(jogador,rival)

        case "4":
            break
