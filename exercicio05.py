# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

try:
    valor = float(input('Digite um valor inteiro: '))
    print(f'O quadrado do valor é: {valor ** 2:.2f}')
except (ValueError, TypeError):
    print("Você não digitou um número inteiro")
    exit()