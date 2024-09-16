peso = int(input("Quantos quilos de peixe? "))
excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Você está com {excesso:} em excesso, e deve pagar {multa: .2f} em multas")
else:
    print(f"Você está com excesso de, {excesso:}, e deve pagar, {multa:}")
