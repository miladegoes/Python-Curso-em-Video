"""
022
Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

nome = str(input('Insira um nome qualquer: '))

print('Letras maiúsculas: {}'.format(nome.upper())) # .upper() deixa os caracteres em caixa alta
print('Letras minúsculas: {}'.format(nome.lower())) # .lower() deixa os caracteres em minusculas
print('Total de letras: {}'.format(len(nome) - nome.count(' '))) #.count(' ') conta os espaços para serem subtraidos
print('Total de letras do primeiro nome: {}'.format(nome.find(' '))) # .find(' ') conta até o primeiro espaço