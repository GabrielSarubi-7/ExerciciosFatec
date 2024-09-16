import random
lista = random.sample(range(100), 20)
par=[]
impar=[]
for x in lista[1:]:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
print('Lista original: ', lista)
print('Pares: ', par)
print('impares: ', impar)

