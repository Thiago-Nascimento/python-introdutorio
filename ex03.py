soma = float(0)
media = float()

for i in range(5):
    numero = float(input("Digite um numero: "))
    soma += numero

print(f"A soma é: {soma}")

media = soma / 5

print(f"A média é igual à: {media}")
