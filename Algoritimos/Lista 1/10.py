Cd = int(input('Quantidade diaria de cigarros '))
#^Cigarros por dia
A = int(input('Quantidade de anos totais fumando '))
#Anos fumando
Vp = ((Cd * 10) * (A * 365)) / 24 / 60
#Vida perdida em dias
print(f'Você perdeu {Vp: .1f} dias')
#Esse eu achei MUITO mais dificil do que os anteriores
