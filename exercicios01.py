 # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

try:
    valor1 = int(input('Digite um valor inteiro: '))
    valor2 = int(input('Digite outro valor inteiro: '))
    print(f'A soma dos valores é: {valor1+valor2}')
except (ValueError, TypeError):
    print("Você não digitou um número inteiro")
    exit()