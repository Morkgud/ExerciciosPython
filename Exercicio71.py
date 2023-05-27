print("======"*6)
print("            BANCO CEV")
print("======"*6)

valor = 0
nota1 = 1
nota10 = 10
nota20 = 20
nota50 = 50

while True:
    valor = int(input("Que valor você quer sacar? R$"))

    # Contagem das notas
    cedulas50 = valor // nota50
    valor = valor % nota50

    cedulas20 = valor // nota20
    valor = valor % nota20

    cedulas10 = valor // nota10
    valor = valor % nota10

    cedulas1 = valor

    # Exibição das notas
    if cedulas50 > 0:
        print("Total de {} cédulas de R$50 reais".format(cedulas50))
    if cedulas20 > 0:
        print("Total de {} cédulas de R$20 reais".format(cedulas20))
    if cedulas10 > 0:
        print("Total de {} cédulas de R$10 reais".format(cedulas10))
    if cedulas1 > 0:
        print("Total de {} cédulas de R$1 real".format(cedulas1))

    opcao = input("Deseja realizar outro saque? [S/N] ").upper()
    if opcao == "N":
        break
print("======"*6)
print("Volte sempre ao nosso banco!")


