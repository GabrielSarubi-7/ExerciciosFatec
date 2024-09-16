area = int(input("Area em metros quadrados "))
lata = int((area / 3) / 18)
if (area / 3) % 18 != 0:
    lata = lata + 1
    print("Você precisará comprar ",lata, "que sairá por ",lata * 80)
else:
    print("Você precisará comprar ",lata, "latas que sairá por ",lata * 80)

#que codigo dos infernos : )
