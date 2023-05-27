cont = 0
for c in range(1, 6):
    cont += 1
    peso = float(input("insira o {}ª peso: ".format(cont)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("O maior peso é {} e o menor peso é {}".format(maior, menor))

