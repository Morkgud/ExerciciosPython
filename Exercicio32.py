ano = int(input("Qual ano você deseja analisar? "))

if ano % 4 == 0:
    print("O ano {} é BISSEXTO!".format(ano))
else:
    print("O ano {} não é BISSEXTO!".format(ano))
