numeros = ()
cont = 0
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite o último número: "))
numeros = (num1, num2, num3, num4)

print(f"\nVocê digitou os números {numeros}")
print(f"O número 9 apareceu {numeros.count(9)} vezes")
print(f"O número 3 foi digitado na posição {numeros.index(3)}")
numeros_pares = tuple(num for num in numeros if num % 2 == 0)
numeros_pares_string = ", ".join(str(num) for num in numeros_pares)

print(f"Números pares digitados: ({numeros_pares_string})")


