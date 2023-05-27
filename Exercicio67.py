print("----" * 12)
num = int(input("Você quer ver a tabuada de qual valor? "))

while num >= 0:
    print("----" * 12)
    for c in range(1, 11):
        tabuada = num * c
        print("{} X {} = {}".format(num, c, tabuada))
    print("----" * 12)
    num = int(input("Você quer ver a tabuada de qual valor? "))

print("Programa de tabuada encerrado")

