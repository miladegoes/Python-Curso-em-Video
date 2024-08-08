"""
018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians


angulo = float(input('Insira um ângulo: '))
# converte o ângulo para radianos para que o cálculo possa ser realizado corretamente
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tang = tan(radians(angulo))

print('O ÂNGULO {}° possui:'.format(angulo))
print('SENO de {:.2f}'.format(seno))
print('COSSENO de {:.2f}'.format(cosseno))
print('TANGENTE de {:.2f}'.format(tang))

