import random

nomes = [input("digite o nome 1: "),
         input("digite o nome 2: "),
         input("digite o nome 3: "),
         input("digite o nome 4: ")]

random.shuffle(nomes)

nome_escolhido = random.choice(nomes)

print("o nome escolhido foi: {}".format(nome_escolhido))


