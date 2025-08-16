# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

try:
    raio = float(input('Digite o raio do círculo: '))
    area = math.pi * (raio ** 2)
    print(f'A área do círculo é: {area:.2f}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()