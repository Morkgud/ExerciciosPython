from random import randint
from time import sleep

NumComp = randint(0, 5)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Eu vou pensar em um número de 0 a 5, tente adivinhar...")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
r = int(input("Em qual número eu pensei? "))

print("")

print("Processando...")
sleep(3)

print("")

print("pensei no número {}".format(NumComp))

if r == NumComp:
    print("Resposta correta, você ganhou!")
else:
    print("Resposta errada, eu ganhei!")





