print("______" * 8)
print("              LOJA SUPER BARATÃO                 ")
print("______" * 8)

produto = ''
preco = 0
cont = 0
cont_preco = 0
produtos = {}

while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço: "))
    cont_preco += preco
    continuar = input("Quer continuar? [S/N] ").upper()

    while continuar not in ["S", "N"]:
        print("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")
        continuar = input("Quer continuar? [S/N] ").upper()

    if preco > 1000:
        cont += 1

    produtos[produto] = preco

    print("______" * 8)

    if continuar == "N":
        break

produto_mais_barato, preco_mais_barato = min(produtos.items(), key=lambda x: x[1])

print("_______________FIM DO PROGRAMA _______________")
print("O total da compra foi de R${}".format(cont_preco))
print("Temos {} produtos custando mais que R$1000.00".format(cont))
print("O produto mais barato foi {} que custa R${}".format(produto_mais_barato, preco_mais_barato))
