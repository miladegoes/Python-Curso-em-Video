"""
027
Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadamente.
"""

# split() divide a string em uma lista de palavras, separando-as pelos espaços em branco
# cada palavra do nome completo se torna um elemento da lista nome
nome= str(input(('Forneça um nome completo: '))).strip().split()
print('Primeiro nome: {}'.format(nome[0])) # acessa o primeiro elemento da lista nome
print('Segundo nome: {}'.format(nome[len(nome)-1])) # acessa o último elemento da lista nome