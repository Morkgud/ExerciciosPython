import datetime

ano = int(input("Digite o seu ano nascimento: "))

idade = datetime.datetime.now().year - ano

print("A sua idade atual é de {} anos".format(idade))

if idade == 18:
    print("Está na hora de se alistar!")
elif idade > 18:
    print("Você ja deveria ter se alistado a {} ano(s)!".format(idade - 18))
else:
    print("Ainda faltam {} ano(s) para você se alistar!".format(18 - idade))


