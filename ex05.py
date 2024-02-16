# Faça um programa que mostre as tabuadas dos números de 1 a 10 usando
# laços de repetição.

for numero in range(1, 11):
    print(f"Essa é a tabuada do {numero}: ")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")