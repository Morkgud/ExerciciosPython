#from random import randint
#print("==============JOGO DE PEDRA, PAPEL E TESOURA==============")
#print("[1] PEDRA")
#print("[2] PAPEL")
#print("[3] TESOURA")

#jogador = int(input("Qual a sua opção: "))

#computador = randint(1, 3)

#if jogador == computador:
    #print("EMPATE")
#elif jogador == 1 and computador == 3:
    #print("VOCÊ VENCEU")
#elif jogador == 1 and computador == 2:
    #print("VOCÊ PERDEU")
#elif jogador == 2 and computador == 3:
    #print("VOCÊ PERDEU")
#elif jogador == 2 and computador == 1:
    #print("VOCÊ VENCEU")
#elif jogador == 3 and computador == 2:
    #print("VOCÊ VENCEU")
#elif jogador == 3 and computador == 1:
    #print("VOCÊ PERDEU")
#else:
    #print("INSIRA UM OPÇÃO VÁLIDA")

#print("O computador escolheu {}!".format(computador))

import random

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

print("==============JOGO DE PEDRA, PAPEL E TESOURA==============")
print("PEDRA")
print("PAPEL")
print("TESOURA")

jogador = input("ESCOLHA UMA DAS OPÇÕES: ")

computador = random.choice(opcoes)

print("O computador escolheu: {}".format(computador))

if jogador == computador:
    print("Empate!")
elif jogador == "PEDRA" and computador == "TESOURA":
    print("Jogador ganha!")
elif jogador == "PAPEL" and computador == "PEDRA":
    print("Jogador ganha!")
elif jogador == "TESOURA" and computador == "PAPEL":
    print("Jogador ganha!")
else:
    print("Insira uma opção válida.")
