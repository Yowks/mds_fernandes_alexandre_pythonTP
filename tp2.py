nomDonne = int(input('Entrez un nombre : '))
factorielle = 1
for i in range(1, nomDonne+1):
    factorielle = factorielle * i
print (nomDonne,': ',factorielle)