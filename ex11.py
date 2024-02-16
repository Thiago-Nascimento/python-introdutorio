# Um funcionário de uma empresa recebe aumento salarial anualmente:

# Sabe-se que:

# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;

# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
# dobro do percentual do ano anterior. Faça um programa que determine o
# salário atual desse funcionário. 

# Após concluir isto, altere o programa
# permitindo que o usuário digite o salário inicial do funcionário.

# 1995 -> 1000
# 1996 -> 1015 (1,5)
# 1997 -> 1015 (3,0)
# ...

salario_inicial = float(1000)

salario = float(1000)
bonus = 0.015

ano_inicial = int(input("Digite o ano inicial: "))

print(f"Em {ano_inicial}, o salario era: {salario}")

for ano in range(ano_inicial + 1, 2025):
    salario = salario_inicial + (salario_inicial * bonus)
    bonus = bonus * 2

    print(f"Em {ano}, o salario era: {salario}")