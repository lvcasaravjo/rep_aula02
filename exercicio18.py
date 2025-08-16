#Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    valor = float(input("Digite um valor: "))

    if valor > 0:
        valor_pos = "positivo"
    elif valor < 0:
        valor_pos = "negativo"
    else:
        valor_pos = "zero"

    if valor % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"

    print(f"O valor inserido é {valor_pos} e {par_impar}")
    
except ValueError as e:
    print(f"Erro: {e}")