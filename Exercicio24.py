nome = input("Digite o nome da sua cidade: ")

tem_santo = "santo" in nome.lower()

if tem_santo:
    print("Sua cidade possui 'santo' no nome.")
else:
    print("Sua cidade não possui 'santo' no nome.")


