# Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi
# superior a loja B (faturamento = 54000). Se o faturamento atingir esse valor
# mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.

faturamento = float(0)
faturamentoLojaB = float(54000)

for i in range(5):
    faturamento += float(input(f"Digite quanto o cliente {i + 1} gastou: "))

if faturamento > faturamentoLojaB:
    print(f"O faturamento superou o da Loja B em R${faturamento - faturamentoLojaB}!!!")
else:
    print(f"O faturamento foi menor que o da Loja B :(")

    