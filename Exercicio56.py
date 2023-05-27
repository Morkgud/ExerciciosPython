cont = 0
SomaIdade = 0
mulheres_jovens = 0
for c in range(1, 5):
    cont += 1
    print("-----{}ª PESSOA-----".format(cont))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    SomaIdade += idade
    media = SomaIdade / cont
    mulher = sexo == "F"
    homem = sexo == "M"
    if c == 1:
        maior = idade
        nome_maior = nome
        menor = idade
    elif idade > maior and homem:
        maior = idade
        nome_maior = nome
    elif idade < menor and homem:
        menor = idade
    if mulher and idade < 20:
        mulheres_jovens += 1

print("A média das somas de todas as idade é {:.2f} anos".format(media))
print("O homem mais velho se chama {} e tem {} anos".format(nome_maior, maior))
print("Existem {} mulheres com idade inferior a 20 anos".format(mulheres_jovens))



