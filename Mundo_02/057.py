"""
057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str((input('Escreva o sexo de uma pessoa, sendo M para masculino e F para feminino: '))).strip().upper()
while sexo not in ['M','F']: # laço while continua enquanto a entrada não for válida
# informa ao usuário que a entrada é inválida e solicita novamente:
    print('O dado inserido é inválido.')
    sexo = str((input('Por favor, forneça M para masculino ou F para feminino: '))).strip().upper()

print('O sexo inserido foi {}.'.format(sexo))
