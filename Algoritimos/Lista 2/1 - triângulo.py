pl = float(input("Qual o primeiro lado do triangulo "))
sl = float(input("Qual o segundo lado do triangulo "))
tl = float(input("Qual o terceiro lado do triangulo "))
if pl + sl > tl or sl + tl > pl or pl + tl > sl:
    if pl == sl == tl:
        print("O triângulo é equilátero")
    elif pl == sl or sl == tl or  pl == tl:
        print("O triângulo é isósceles")
    elif pl != sl and sl != tl and pl != tl:
        print("O trângulo é escaleno")
else:
    print("Não é possivel formar um triângulo")
