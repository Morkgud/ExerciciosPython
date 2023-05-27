soma = 0
contador = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma += c
print("A soma de todos os {} equivale a {}".format(contador, soma))









