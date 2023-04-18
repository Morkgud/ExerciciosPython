import random

#lista para o professor escolher o nome de quem vai apagar o quadro.
nomes = [input("digite o nome 1: "),
         input("digite o nome 2: "),
         input("digite o nome 3: "),
         input("digite o nome 4: ")]

random.shuffle(nomes)

nome_escolhido = random.choice(nomes)

print("o nome escolhido foi: {}".format(nome_escolhido))

#lista para definir a ordem dos participantes do trabalho.
lista = [1,2,3,4]

random.shuffle(lista)

ordem_escolhida= lista

print("a ordem escolhida foi: {}".format(ordem_escolhida))

