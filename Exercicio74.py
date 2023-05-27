import random

numeros_sorteados = tuple(random.randint(0, 10) for _ in range(5))

print("Números sorteados:", numeros_sorteados)
maior_numero = max(numeros_sorteados)
menor_numero = min(numeros_sorteados)

print("Maior número:", maior_numero)
print("Menor número:", menor_numero)