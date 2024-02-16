# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite o primeiro numero do intervalo: "))
n2 = int(input("Digite o segundo numero do intervalo: "))

for i in range(n1, n2 + 1):
    print(i)