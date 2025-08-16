# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

try:
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite um valor: '))
    operador = input("Digite um operador (+, -, *, /) para realizar o cálculo: ")

    if operador == '+':
        calculo = valor1 + valor2
        operacao = 'soma'
    elif operador == '-':
        calculo = valor1 - valor2
        operacao = 'subtração'
    elif operador == '*':
        calculo = valor1 * valor2
        operacao = 'multiplicação'
    elif operador == '/' and valor2 != 0:
        calculo = valor1 / valor2
        operacao = 'divisão'
    elif operador == '/' and valor2 == 0:
        print("Divisão por zero")
    else:
        raise ValueError("Operador inválido. Use apenas +, -, * ou /.")

    print(f"O resultado da operação de {operacao} é {calculo}")

except ValueError as e:
    print(f"Erro: {e}")



