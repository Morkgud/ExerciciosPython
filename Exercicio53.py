frase = str(input("Digite uma frase: "))

FraseInvertida = frase[::-1]
FraseFinal = FraseInvertida.replace(" ", "")

print("A frase invertida fica desse jeito: {}".format(FraseFinal))

if FraseFinal == FraseFinal[::-1]:
    print("É um palíndromo")
else:
    print("não é um palindromo")
