# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

palavra = input('Digite uma palavra: ')

if palavra.isdigit():
    print('Você digitou um número')
elif palavra.isspace():
    print('Você digitou espaço(s) vazio(s)')
elif isinstance(palavra, str):
    print(palavra.upper())
