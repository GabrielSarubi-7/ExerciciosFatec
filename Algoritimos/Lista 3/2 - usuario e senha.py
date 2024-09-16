nome = int(input("Digite o nome do usuario" ))
senha = int(input("Digite sua senha "))
while nome == senha:
    print("O nome de usuario não pode ser igual a senha")
    senha = int(input("Digite sua senha "))
print("Tudo certo")
