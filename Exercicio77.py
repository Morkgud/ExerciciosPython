palavras = ("APRENDER", "PROGRAMAR", "ESTUDAR", "AGORA", "ENSINAR", "PYTHON", "ARGUS")

for palavra in palavras:
    print(f"\nNa palavra {palavra} existem as vogais", end=" ")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(f"{letra}", end=" ")