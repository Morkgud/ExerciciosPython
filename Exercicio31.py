viagem = float(input("Qual foi a distância percorrida em sua viagem em Km/h? "))

print("Você está prestes a fazer uma viagem de {} Km/h!".format(viagem))

passagem1 = viagem * 0.45
passagem2 = viagem - 200 * 0.50

if viagem >= 200:
    print("E o preço da sua viagem será de {}! ".format(passagem2))
else:
    print("E o preço da sua viagem será de {}!".format(passagem1))
