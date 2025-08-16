# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

try:
    temp_celsius = float(input('Digite a temperatura atual na sua região em Celsius (apenas números): '))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f'A temperatura atual convertida para Fahrenheit é: {temp_fahrenheit}')
except (ValueError, TypeError):
    print("Você não digitou um número")
    exit()