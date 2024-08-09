"""
045
Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random
import time

print('[1] - PEDRA')
print('[2] - PAPEL')
print('[3] - TESOURA')

jogadas = [1, 2, 3]  # define as opções de jogadas em uma lista
jogador = int(input('Sua escolha: '))  # solicita a escolha da jogada do usuário

if jogador not in jogadas:  # verifica se a jogada do jogador é válida
    print("Jogada inválida! Tente novamente.")
else:
    computador = random.choice(jogadas)  # escolhe a jogada do computador

    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ!')

    escolhas = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
    print('-' * 25)
    print('Você jogou c.'.format(escolhas[jogador]))
    print('Computador jogou {}.'.format(escolhas[computador]))
    print('-' * 25)

    if jogador == computador:
        resultado = 'EMPATE!'
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        resultado = 'Você venceu!'
    else:
        resultado = 'Você perdeu!'

    print(resultado)





