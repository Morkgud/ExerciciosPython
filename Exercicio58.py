from random import randint

computador = randint(1, 10)
print("Eu sou seu computador...")
print("Eu vou pensar em um número entre 1 e 10.")
print("Será que você consegue acertar?")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual o seu palpite: "))
    palpite += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print("O número é maior")
    elif jogador > computador:
        print("O número é menor")
print("O número que eu escolhi era {} e você acertou em {} tentativas!".format(computador, palpite))









