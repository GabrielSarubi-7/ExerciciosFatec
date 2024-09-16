import random
lista1 = random.sample(range(1, 100), 10)
lista2 = random.sample(range(1, 100), 10)
lista3 = []

for x in range(10):
    lista3.append(lista1[x])
    lista3.append(lista2[x])


print(lista1)
0,3print(lista2)
print(lista3)
