ano = 0
a = 80000
b = 200000
while a <= b:
    ano = ano + 1
    a = a + (a * (3/100))
    b = b + (b* (1.5/100))
print("São necessarios", ano,"anos")
