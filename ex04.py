# Faça um programa que receba um número e usando laços de repetição
# calcule e mostre a tabuada desse número.

numero = float(input("Digite um numero que deseja saber a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

    