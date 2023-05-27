#salario = float(input("Qual o salário do funcionário? R$"))

#superior= salario *0.10
#inferior= salario *0.15
#total1 = superior + salario
#total2 = inferior + salario

#if salario >= 1250:
   # print("Quem ganhava {}R$ passa a ganhar R${} agora.".format(salario, total1))
#else:
   # print("Quem ganhava {}R$ passa a ganhar R${} agora.".format(salario, total2))

salario = float(input("Qual o salário do funcionário? R$"))

inferior = (salario * 0.15)
superior = (salario * 0.10)

if salario >= 1250:
    print("Quem ganhava {}R$ passa a ganhar R${} agora.".format(salario, superior+salario))
else:
    print("Quem ganhava {}R$ passa a ganhar R${} agora.".format(salario, salario+inferior))


