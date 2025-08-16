# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

try:
    valor1 = float(input('Digite um valor: '))
    expoente = int(input('Digite a potência para o valor ser elevado: '))
    print(f'A potência de {valor1} elevado a {expoente} é igual a {valor1 ** expoente}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()