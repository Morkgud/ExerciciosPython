peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso/altura ** 2
imc_arredondado = round(imc, 2)

print("Seu IMC é {}".format(imc_arredondado))

if imc_arredondado <= 18.5:
    print("ABAIXO DO PESO")
elif imc_arredondado <= 25:
    print("PESO IDEAL")
elif imc_arredondado <= 30:
    print("SOBREPESO")
elif imc_arredondado <= 40:
    print("OBESIDADE")
elif imc_arredondado > 40:
    print("OBESIDADE MÓRBIDA")
