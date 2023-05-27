valores = list()

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

maior_valor = max(valores)
menor_valor = min(valores)

print(f"O maior valor é {maior_valor} e está na posição {valores.index(maior_valor)}.")
print(f"O menor valor é {menor_valor} e está na posição {valores.index(menor_valor)}.")

