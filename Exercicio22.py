nome = input("digite o seu nome completo: ")

nome_sem_espacos = nome.replace(" ", "")

print("seu nome em maiúsculo é: {} ".format(nome.upper()))
print("seu nome em minúsculo é: {} ".format(nome.lower()))
print("seu nome sem espaços é: {}".format(nome_sem_espacos))
print("sem nome sem espaço tem: {} letras".format(len(nome) - nome.count(" ")))
print("seu primeiro nome tem: {} letras".format(nome.find(" ")))
