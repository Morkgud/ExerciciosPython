p = float(input('Preço do produto a prazo: R$'))
desconto = p*5/100
print('Valor com desconto: R${:.2f}'.format(p-desconto))