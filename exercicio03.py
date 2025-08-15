# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try:
    valor1 = float(input('Digite um valor inteiro: '))
    valor2 = float(input('Digite outro valor inteiro: '))
    print(f'A multiplicação dos valores é: {valor1*valor2}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()