"""
003
Crie um programa que leia dois números e mostre a soma entre eles.
"""

print('------= SOMANDO DOIS NÚMEROS =------')

# pede as entradas ao usuário
n1 = int(input('Forneça o primeiro número: '))
n2 = int(input('Forneça o segundo número: '))

# soma os dois valores, armazenando o resultado em outra variável
soma = n1 + n2

print('{} + {} = {}'.format(n1, n2, soma))