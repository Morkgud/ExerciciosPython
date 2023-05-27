from math import factorial

print("Digite um número para")
num = int(input("calcular seu fatorial: "))
fatorial = factorial(num)
c = num
while c > 0:
    print('{}'.format(c), end=" ")
    print("X "if c > 1 else "= ", end="")
    c -= 1
print("{}".format(fatorial))
