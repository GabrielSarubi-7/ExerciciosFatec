nota = int(input('Digite sua nota entre 0 e 10 ' ))
while nota < 0 or nota > 10:
    print("Nota inválida")
    print("Digite um valor válido")
    nota = int(input('Digite sua nota entre 0 e 10 ' )) 
print(nota)
