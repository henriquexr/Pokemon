import random
import classesTreinador
import classesPokemon

#Metodo de batalha

def batalha(pokemon, pokemonRival):
    pokemon = classesTreinador.jogador.escolherPokemon()
    pokemonRival = classesTreinador.rival.pokemonRival()
    vidaInimigo = pokemonRival._hp
    vida = pokemon._hp

    listaDeAtq =["Arranhao", "Rosnar"]

    while vida >0 and vidaInimigo>0:

        print(f'''Escolha seu ataque:
            1.{listaDeAtq[0]}
            2.{listaDeAtq[1]}
            3. Sair
        ''')
        ataque = input(">")
#Menu de escolha de ataque
        match (ataque):
                case "1":
                        print(f"{pokemon._especie} usou {listaDeAtq[0]}")
                        vidaInimigo = vidaInimigo - 2
                case "2":
                        print(f"{pokemon._especie} usou {listaDeAtq[1]}")
                        vidaInimigo = vidaInimigo - 0
                case "3":
                    print("Voçe abandonou a batalha!")
                    break
        print(f"{pokemonRival._especie} está com:{vidaInimigo}HP")
        if vidaInimigo<= 0:
            break
#Jogada do oponente aleatoria
        print(f"{pokemonRival._especie} se preparando pra atacar!")
        ataqueInimigo = random.choice(listaDeAtq)
        match (ataqueInimigo):
                case "Arranhao":
                    print(f"{pokemonRival._especie} usou {listaDeAtq[0]}")
                    vida = vida - 2
                case "Rosnar":
                    print(f"{pokemonRival._especie} usou {listaDeAtq[1]}")
                    vida = vida - 0
        print(f"{pokemon._especie} está com:{vida}HP\n")
#verificaçao de vitoria
    if vida>0 and vidaInimigo <=0:
        print(f"{pokemon._especie}, Ganhou a batalha")
    else:
        print(f"{pokemon._especie}, perdeu!")
