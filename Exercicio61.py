print("=+=+="*6)
print("     OS TERMOS DE UMA PA            ")
print("=+=+="*6)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} --> ".format(termo), end="")
    termo += razao
    cont += 1
print("Fim")
