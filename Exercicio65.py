resp = "S"
cont = soma = media = 0
menor = 0
maior = 0
primeiro = True

while resp in "S":
    num = int(input("Digite um número: "))
    resp = str(input("Deseja continuar?[S/N]: ").upper())
    cont += 1
    soma += num
    media = soma / cont
    if primeiro:
        menor = maior = num
        primeiro = False
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
print("a média de todos os números equivale a {} e você colocou {} números".format(media, cont))
print("O menor número é {} e o maior número é {}.".format(menor, maior))





