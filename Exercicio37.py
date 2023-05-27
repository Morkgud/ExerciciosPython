num = int(input("digite um número inteiro: "))

print("Escolha uma das bases numéricas para a conversão:")

print("[1] Converter para o BINÁRIO")
print("[2] Converter para o OCTAL")
print("[3] Converter para o HEXADECIMAL")

resposta = int(input("Sua opção: "))

binario = bin(num).replace("0b", "")
octal = oct(num).replace("0o", "")
hexadecimal = hex(num).replace("0x", "")

if resposta == 1:
    print("O número {} convertido para BINÁRIO é igual a {}".format(num, binario))

elif resposta == 2:
    print("O número {} convertido para OCTAL é igual a {}".format(num, octal))

elif resposta == 3:
    print("O número {} convertido para HEXADECIMAL é igual a {}".format(num, hexadecimal))
else:
    print("Digite um dos números informados")

