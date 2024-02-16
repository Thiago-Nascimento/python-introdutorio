maior_valor = float()

for i in range(5):
    numero = float(input("Digite um número: "))

    if numero > maior_valor:
        maior_valor = numero

    print(f"Atualmente o maior numero é {maior_valor}")