"""
002
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""

# pede a entrada ao usuário, eliminando espaços desnecessários e deixando a string em maiúscula
nome = str(input('Qual o seu nome? Insira a seguir: ')).strip().upper()

# imprime a mensagem
print('Olá {}, é um prazer ter você aqui! ♡'.format(nome))