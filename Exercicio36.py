casa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 0.30

print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos), end='')
print(" será necessário uma prestação de R${:.2f}".format(prestacao))

if prestacao >= minimo:
    print("Empréstimo negado")
else:
    print("Empréstimo permitido")









