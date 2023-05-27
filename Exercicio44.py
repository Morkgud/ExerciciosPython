print("=======================LOJINHA=======================")
compras = float(input("preço das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("[1] à vista em dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

opcao = int(input("Qual a sua opção: "))

dc = (compras * 10/100)
c = (compras * 5/100)
duas = compras
mais = (compras * 20/100)

if opcao == 1:
    preco_final = compras - dc
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(compras, preco_final))
elif opcao == 2:
    preco_final = compras - c
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(compras, preco_final))
elif opcao == 3:
    preco_final = duas / 2
    print("Sua compra de R${:.2f} vai custar 2x de R${:.2f} no final.".format(compras, preco_final))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    preco_final = mais / parcelas
    print("Sua compra de R${:.2f} vai custar {}x de R${:.2f} no final.".format(compras, parcelas, preco_final))
else:
    print("Opção inválida.")



