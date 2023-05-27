import datetime

ano = int(input("Ano de nascimento:"))

idade = datetime.datetime.now().year - ano

print("Sua idade é {}!".format(idade))
print("E a sua categoria é: ")

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 25:
    print("SENIOR")
elif idade > 25:
    print("MASTER")
