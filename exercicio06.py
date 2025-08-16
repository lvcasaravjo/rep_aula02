# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

try:
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro valor: '))
    print(f'A soma dos valores é: {valor1+valor2}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()