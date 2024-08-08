"""
028
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça:
- para o usuário tentar descobrir qual foi o número escolhido pelo computador;
- o programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint # randint é a função que irá sortear o número do computador

print('-=-' * 7)
print('JOGO DE ADIVINHAÇÃO')
print('-=-' * 7)
computador = randint(0, 5)
jogador = int(input('De 0 a 5, em qual número estou pensando? ➔ '))

if jogador == computador: # se jogador for igual a computador...
    print('(,,>﹏<,,) ➔ Você acertou! Eu realmente estava pensando no número {}...'.format(jogador))
else: # se não for...
    print('( ˶ˆᗜˆ˵ ) ➔ Ganhei! Eu estava pensando no número {}!'.format(computador))
