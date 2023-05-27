lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print("Esse valor já foi adicionado, Tente novamente!")
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso!")

    resposta = input("Você quer continuar? [S/N]: ").upper()
    if resposta != "S":
        break
print("=-=-=-="*5)
lista.sort()
print(lista)