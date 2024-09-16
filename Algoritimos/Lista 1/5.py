V = int(input('Valor da mercadoria '))
D = int(input('Quantidade de desconto em porcentagem '))
Db = V * D / 100
#^Desconto bruto
Pt = V - Db
#^Preço total
print('O valor do desconto é de: ', Db, ' O valor total fica em: ', Pt)
