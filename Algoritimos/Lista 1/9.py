K = int(input('Quantidade de Kilometros percorridos '))
#^Kilometros percorridos
D = int(input('Quantidade de dias com o carro '))
#^Dias totais
P = (K * 0.15) + (D * 60)
#^Preço total
print(f'O valor do carro será de: R${P: .2f}')
