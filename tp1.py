x=range(2000,3200)
numbers=[]
for number in x :
    resultBySeven = number % 7
    if resultBySeven == 0 :
        resultNotByFive = number % 5
        if resultNotByFive != 0 :
            numbers.append(number)
    number = number + 1

print(numbers)