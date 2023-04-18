numero = int(input("digite um número de 1 a 9999: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena= numero // 100 % 10
milhar= numero // 1000 % 10

print("analisando o número {}, percebemos que ele possui: ".format(numero))
print("unidade: {}".format(unidade))
print("dezena: {}".format(dezena))
print("centena: {}".format(centena))
print("milhar: {}".format(milhar))
