"""
004
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

# pede a entrada ao usuário
entrada = input('Digite qualquer coisa: ')

# mostra o tipo primitivo da entrada
print('Tipo primitivo: {}'.format(type(entrada)))

# exibe as informações sobre a entrada; \n quebra a linha.
print('É um número? \n{}'.format(entrada.isnumeric()))
print('É alfabético? \n{}'.format(entrada.isalpha()))
print('É alfanumérico? \n{}'.format(entrada.isalnum()))
print('Só tem espaços? \n{}'.format(entrada.isspace()))
print('Está em maiúsculas? \n{}'.format(entrada.isupper()))
print('Está em minúsculas? \n{}'.format(entrada.islower()))
print('Está capitalizada? \n{}'.format(entrada.istitle()))

