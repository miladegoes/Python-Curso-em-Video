"""
058
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint  # randint é a função que irá sortear o número do computador

print('-=-' * 7)
print('JOGO DE ADIVINHAÇÃO')
print('-=-' * 7)

computador = randint(0, 5)
palpites = 0 # inicia a variável para armazenar a qnt de palpites
acertou = False # inicia a variável para armazenar o valor de V ou F.

while not acertou: #  o laço while continua até que a variável 'acertou' seja 'true'
    jogador = int(input('De 0 a 5, em qual número estou pensando? ➔ '))
    palpites += 1 # a cada iteração do laço while, o valor de palpites será aumentado em 1
    if jogador == computador:
        acertou = True
        print('(,,>﹏<,,) ➔ Você acertou! Eu realmente estava pensando no número {}...'.format(jogador))
    else:
        print('( ˶ˆᗜˆ˵ ) ➔ Errado! Tente novamente.')

print('-' * 45)
print('Você precisou de {} palpites para acertar.'.format(palpites))

