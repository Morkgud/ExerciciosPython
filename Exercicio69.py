print("-----" * 5)
print("Cadastre uma pessoa")
print("-----" * 5)

cont_mulher = 0
cont_homem = 0
cont = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F] ").upper()
    print("-----" * 5)

    continuar = input("Quer continuar? [S/N] ").upper()

    while continuar not in ["S", "N"]:
        print("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")
        continuar = input("Quer continuar? [S/N] ").upper()

    if idade > 18:
        cont += 1
    if sexo == "M":
        cont_homem += 1
    elif sexo == "F":
        if idade < 20:
            cont_mulher += 1
    else:
        print("Opção de sexo inválida. Digite 'M' para Masculino ou 'F' para Feminino.")

    if continuar == "N":
        break

print("{} pesso(as) têm mais de 18 anos".format(cont))
print("{} homen(s) foram cadastrados".format(cont_homem))
print("{} mulher(es) têm menos de 20 anos".format(cont_mulher))