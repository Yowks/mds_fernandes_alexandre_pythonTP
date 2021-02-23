def compteur(number):
    i = 0
    while i <= int(number):
        result = i % 7
        if result == 0:
            print(i)
        i = i + 1

number = int(input('nombre : '))
compteur(number)