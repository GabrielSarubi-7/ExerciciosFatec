n1 = int(input("Digite o primeiro numero "))
n2 = int(input("Digite o segundo numero "))
n3 = int(input("Digite o terceiro numero "))

if n1 >= n2 and n1 >= n3:
    if n2 < n3:
        print("O maior numero é ", n1, "e o menor é ", n2)
    else:
        print("O maior numero é ", n1, "e o menor é ", n3)
             
elif n2 >= n1 and n2 >= n3:
    if n1 < n3:
        print("O maior numero é ", n2, "e o menor é ", n1)
    else:
        print("O maior numero é ", n2, "e o menor é ", n3)
    
else:
    if n1 <= n2:
        print("O maior numero é ", n3, "e o menor é ", n1)
    else:
        print("O maior numero é ", n3, "e o menor é ", n2)
