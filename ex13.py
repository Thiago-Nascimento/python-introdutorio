# Uma loja tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.

# Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…

# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valordacompra – porcentagem de desconto – valor final

valor_compra = float(input("Digite qual foi o valor da compra do cliente: "))

if valor_compra > 500:
    porcentagem_desconto = int(valor_compra / 100) - 4

    valor_final = valor_compra - (valor_compra * (porcentagem_desconto / 100))

    print(f"R$800{valor_compra} - {porcentagem_desconto}% - R${valor_final}")

else:
    print("Valor muito baixo para desconto :(")

