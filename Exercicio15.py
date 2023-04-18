dias = int(input("Quantos dias o carro foi alugado: "))
km = float(input("Quantos km foram rodados com esse carro: "))

pago = (dias * 60) + (km * 0.15)

print("o preço a pagar pelos dias alugados será de: {}".format(pago))

