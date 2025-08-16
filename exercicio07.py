# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

import numpy as np

try:
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro valor: '))
    media_valores = (valor1 + valor2)/2
    print(f'A média entre os valores é {media_valores}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()