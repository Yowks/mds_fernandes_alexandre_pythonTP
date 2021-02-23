tab = []
i=0
sentence = input('Vos mots : ')
sentence = sentence.replace(",", "")
split = sentence.split()
sortedsentence = sorted(split)
final = ", ".join(sortedsentence)
print(final)