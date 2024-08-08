"""
020
#  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle # importa a função shuffle para sortear uma ordem de uma lista

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))

lista = [a1, a2, a3, a4] # coloca os nomes inseridos pelo usuário em uma lista
shuffle(lista) # randomiza a senquência
print('Ordem de apresentação: ')
print(lista)
