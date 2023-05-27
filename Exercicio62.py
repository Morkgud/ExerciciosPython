print("=+=+="*6)
print("     OS TERMOS DE UMA PA            ")
print("=+=+="*6)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} --> ".format(termo), end="")
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Mais quantos termos você quer adicionar: "))
print("Fim da progressão aritmética e {} termos foram mostrados".format(total))

