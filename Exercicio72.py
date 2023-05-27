cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze',
        "treze", 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
cn = 0
while True:
    num = int(input("Digite um número entre 0 a 20: "))
    if 0 <= num <= 20:
        print(f'você digitou o número {cont[num]}')
    else:
        print("Tente novamente. ", end="")
    novamente = str(input("quer continuar? [S/N] ")).upper()
    cn += 1
    if novamente != "S":
        break
print(f"Obrigado por usar o nosso programa, você digitou {cn} números!")


