# Faça um programa que receba a idade de 15 pessoas e que calcule e
# mostre:

# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com relação
# ao total de pessoas:

# - Até 15 anos
# - De 16 a 30 anos
# - De 31 a 45 anos
# - De 46 a 60 anos
# - Acima de 61 anos

num_pessoas = 15

ate_15 = 0
de_16_ate_30 = 0
de_31_ate_45 = 0
de_46_ate_60 = 0
mais60 = 0

for i in range(num_pessoas):
    idade = int(input(f"Digite a idade da {i + 1}º pessoa: "))

    if idade <= 15:
        ate_15 += 1
    elif idade > 15 and idade <= 30:
        de_16_ate_30 += 1
    elif idade > 30 and idade <= 45:
        de_31_ate_45 += 1
    elif idade > 45 and idade <= 60:
        de_46_ate_60 += 1
    else:
        mais60 += 1

print(f"\nPessoas até 15 anos: {ate_15}")
print(f"Pessoas de 16 à 30 anos: {de_16_ate_30}")
print(f"Pessoas de 31 à 45 anos: {de_31_ate_45}")
print(f"Pessoas de 46 à 60 anos: {de_46_ate_60}")
print(f"Pessoas com mais de 60 anos: {mais60}\n")

print(f"Porcentagem até 15 anos: {(ate_15 / num_pessoas) * 100}%")
print(f"Porcentagem mais 60 anos: {(mais60 / num_pessoas) * 100}%\n")