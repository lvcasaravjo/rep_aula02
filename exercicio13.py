# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input('Digite uma frase: ')

if frase.isdigit():
    print('Você digitou um ou mais números')
elif frase.isspace():
    print('Você digitou espaço(s) vazio(s)')
elif isinstance(frase, str):
    print(frase.strip())
