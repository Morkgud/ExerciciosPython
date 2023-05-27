'''pessoa = input("Digite o seu gênero [M/F]: ").upper()

while pessoa != "M" and pessoa != "F":
    print("Gênero inválido. Digite novamente.")
    pessoa = input("Digite o seu gênero [M/F]: ").strip().upper()[0]
print("Programa encerrado. Obrigado por usar nosso sistema!")'''

pessoa = str(input("Digite seu gênero [M/F]: ")).strip().upper()[0]

while pessoa not in "MmFf":
    print("Gênero inválido, digite novamente")
    pessoa = str(input("Digite seu gênero [M/F]: ")).strip().upper()[0]
print("Gênero {} foi salvo, obrigado por usar nosso programa".format(pessoa))



