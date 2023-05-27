nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1+nota2) / 2

print("Sua nota foi de {} pontos".format(media))

if media <= 5.0:
    print("Você está reprovado!")
elif media >= 7.0:
    print("Você passou!")
elif media >= 5.0:
    print("Você está de recuperação!")
