import math
from math import sqrt

cateto1 = int(input("digite o comprimento do cateto1: "))
cateto2 = int(input("digite o comprimento do cateto2: "))

triangulo_retangulo = sqrt(cateto1*cateto1 + cateto2*cateto2)

print("o comprimento da hipotenusa é de: {}".format(math.floor(triangulo_retangulo)))
