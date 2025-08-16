# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, 
# desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

palavra = input('Digite uma palavra: ')
palavra_invertida = palavra[::-1]


if palavra.isdigit():
    print('Você digitou um número')
elif palavra.isspace():
    print('Você digitou espaço(s) vazio(s)')
elif isinstance(palavra, str) and palavra == palavra_invertida:
    print(f"A palavra {palavra} é um palíndromo")
elif isinstance(palavra, str) and palavra != palavra_invertida:
    print(f"A palavra {palavra} não é um palíndromo")
elif palavra.isdigit():
    print('Você digitou um número')
elif palavra.isspace():
    print('Você digitou espaço(s) vazio(s)')
