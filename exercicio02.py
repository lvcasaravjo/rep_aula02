# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

try:
    valor1 = float(input('Digite um valor inteiro: '))
    resto = valor1 % 5
    print(f'O resto da divisão do valor por 5 é: {resto}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()