a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

menor = a
if b<a and b<c:
    menor= b
if c<a and c<b:
    menor= c
print("o menor valor é {}".format(menor))

maior = a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior= c
print("o maior valor é {}".format(maior))
