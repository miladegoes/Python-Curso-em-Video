"""
019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

from random import choice # importa a função choice para sortear um item de uma lista

a1 = str(input('Insira o nome do primeiro aluno: '))
a2 = str(input('Insira o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))

lista = [a1, a2, a3, a4] # coloca os nomes inseridos pelo usuário em uma lista
sorteado = choice(lista) # sorteia 1 item aleátorio da lista
print('Aluno escolhido: {}'.format(sorteado))
