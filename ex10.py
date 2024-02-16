# Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números impares.

num_pares = int(0)
num_impares = int(0)

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º numero: "))

    if numero % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print(f"Você digitou {num_pares} numeros pares, e {num_impares} numeros ímpares")