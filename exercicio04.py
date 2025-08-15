# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    valor1 = int(input('Digite um valor inteiro: '))
    valor2 = int(input('Digite outro valor inteiro: '))
    print(f'A divisão inteira dos valores é: {valor1//valor2}')
except (ValueError, TypeError):
    print("Você não digitou um número inteiro")
    exit()