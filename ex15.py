# Faça um programa que peça dois números, base e expoente, calcule e
# mostre o primeiro número elevado ao segundo número. Não utilize a
# função de potência da linguagem.

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = int()

if expoente == 0:
    resultado = 1
elif expoente == 1:
    resultado = base
elif expoente > 1:
    resultado = base

    for i in range(expoente - 1):
        resultado = resultado * base

print(f"\nO resultado é: {resultado}\n")