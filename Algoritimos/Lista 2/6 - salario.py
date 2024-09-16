salariohora = int(input("Qual seu salario por hora? "))
horames = int(input("Quantas horas de trabalho mensal? "))
salariomes = salariohora * horames
print("Seu salario bruto é de ",salariomes)

print(f"O valor a ser pago ao imposto de renda (11%) é {salariomes * 0.11: .2f}")


print(f"O valor a ser pago ao INSS (8%) é {salariomes * 0.08: .2f}")


print(f"O valor a ser pago ao Sindicato (5%) é {salariomes * 0.05: .2f}")

salariomes = (((salariomes * 0.95)* 0.92)* 0.89)
print(f"Seu salario liquido é de {salariomes:.2f}")
