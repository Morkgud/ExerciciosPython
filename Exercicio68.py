import random
from time import sleep

print("-=-=-=-" * 6)
print("VAMOS JOGAR PAR OU ÍMPAR!")
print("-=-=-=-" * 6)
computador = random.randint(1, 10)  # Intervalo de 1 a 10
cont = 0
ganhar = True

while ganhar:
    usuario = int(input("Diga um valor: "))
    pi = input("Par ou ímpar? [P/I]").upper()
    resposta = usuario + computador
    print("Você jogou {} e o computador jogou {}".format(usuario, computador))
    print("A soma dos valores é {}".format(resposta))

    if resposta % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    if resultado == pi:
        print("Você venceu!")
        cont += 1
    else:
        print("Você perdeu!")
        break
    print("-" * 30)

sleep(1)
print("Você venceu {} vez(es) consecutiva(s)".format(cont))

#variaveis
#computador
#usuario
#pi
#cont
#ganhar
#resposta

