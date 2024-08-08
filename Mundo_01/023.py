"""
023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

# converte o número para string para facilitar a separação dos dígitos. zfill(4) garante que string tenha 4 caracteres
numero = str(input('Insira um número de 0 a 9999: ')).zfill(4)

print('Analisando o número {}...'.format(numero))

print('Sua unidade é: {}'.format(numero[3]))
print('Sua dezena é: {}'.format(numero[2]))
print('Sua centena é: {}'.format(numero[1]))
print('Seu milhar é: {}'.format(numero[0]))