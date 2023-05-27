print("-=-"*11)
print("Analisador de Triângulos")
print("-=-"*11)

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima NÃO podem formar um triângulo!")

