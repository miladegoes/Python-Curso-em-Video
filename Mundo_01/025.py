"""
025
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome = str(input('Digite um nome completo: ')).strip().lower()
print('Essa esse nome possui o sobrenome Silva? ➔ {}'.format('silva' in nome))
