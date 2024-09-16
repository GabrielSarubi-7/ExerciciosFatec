n1 = int(0)
n2 = int(0)
n3 = int(1)
tempo = 0
tempototal = int(input("Quantos numeros de fibonacci? "))
while tempo != tempototal:
    n1 = n3 + n2
    n2 = n3
    n3 = n1
    print(n2)
    tempo = tempo + 1
print("pronto")
