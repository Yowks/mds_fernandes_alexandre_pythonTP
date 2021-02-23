number = int(input('Entrez un nombre : '))
dictionnaire={}
for i in range(1, number+1):
    dictionnaire[i] = i * i
print (dictionnaire)