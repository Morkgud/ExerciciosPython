from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
usuario = 0
while usuario != 5:
    print("===" * 9)
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")
    usuario = int(input(">>>>>>>>> Qual a sua opção? "))
    soma = num1 + num2
    mult = num1 * num2
    if usuario == 1:
        print("A soma entre {} e {} equivale a {}".format(num1, num2, soma))
    elif usuario == 2:
        print("A multiplicação entre {} e {} equivale a {}".format(num1, num2, mult))
    elif usuario == 3:
        if num1 > num2:
            print("{} é maior que {}".format(num1, num2))
        else:
            print("{} é menor que {}".format(num1, num2))
    elif usuario == 4:
        print("Informe os números novamente: ")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    else:
        print("Opção inválida, tente novamente.")
print("\33[32mFinalizando...")
sleep(1.5)
print("\33[34mObrigado por usar o nosso programa!")





