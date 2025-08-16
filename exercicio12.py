# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

primeiro_nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')

if primeiro_nome.isdigit() or sobrenome.isdigit():
    print('Você digitou um ou mais números')
elif primeiro_nome.isspace() or sobrenome.isspace():
    print('Você digitou espaço(s) vazio(s)')
elif isinstance(primeiro_nome, str) and isinstance(sobrenome, str):
    print(primeiro_nome.upper()+' '+sobrenome.upper())
