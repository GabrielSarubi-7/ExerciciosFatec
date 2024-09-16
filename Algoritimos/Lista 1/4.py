S = int(input("Quantidade original do salario "))
P = int(input("Porcentagem de aumento "))
A = S * P / 100
#^aumento bruto
N = S + A
#^novo salario
print('Seu salario aumentou em ', A , 'O valor total é ', N)
