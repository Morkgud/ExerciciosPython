import datetime

soma = 0
cont = 0

for c in range(1, 8):
    ano = int(input("Digite o ano do seu nascimento: "))
    idade = datetime.datetime.now().year - ano

    if idade >= 21:
        soma += idade
        cont += 1

print("Ao todo tivemos {} pessoas maiores de idade com uma média de {} anos".format(cont, soma / cont))
print("Também tivemos {} pessoas menores de idade".format(7 - cont))



