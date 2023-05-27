import math

velocidade = float(input("Qual a velocidade atual de um carro? "))

limite = 80-1

DistanciaUltrapassada = velocidade - limite

multa = DistanciaUltrapassada * 7

if velocidade >= 80:
    print("Você ultrapassou o limite de velocidade de 80 KM/h e você deve pagar uma multa de {}!".format(multa))
else:
    print("Tenha um bom dia!")