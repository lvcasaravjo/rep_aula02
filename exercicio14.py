# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data no formato 'dd/mm/aaaa': ")

print(F"Ano digitado: {data.split('/')[2]}")
print(F"Mês digitado: {data.split('/')[1]}")
print(F"Dia digitado: {data.split('/')[0]}")