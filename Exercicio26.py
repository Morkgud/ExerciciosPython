nome = input("digite uma frase: ")

print("A letra A aparece: {} vezes".format(nome.count("a")))
print("A primeira letra A apareceu na posição: {}".format(nome.find("a")+1))
print("A última letra A apareceu na posicão: {}".format(nome.rfind("a")+1))



