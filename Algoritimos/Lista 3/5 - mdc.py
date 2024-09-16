n1 = float(input("Digite o primeiro numero inteiro positivo "))
n2 = float(input("Digite o segundo numero inteiro positivo "))


A = float(n1)
B = float(n2)

while A % B != 0:
    resto = A % B
    A = B
    B = resto;
else:
    print(f"O MDC de {n1} e {n2} é {resto}")
