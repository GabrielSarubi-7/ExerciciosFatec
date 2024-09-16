import random
lista = random.sample(range(1, 100), 10)
maior = lista[0]
menor = lista[0]
for x in  lista[1:]:
    if x > maior: maior = x
    if x < menor: menor = x
print("Lista: ", lista, 'o maior é:', maior, "o menor é:", menor)
