"""
017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot # importa a função de hipotenusa

cat_oposto = float(input('Comprimentento do cateto oposto: '))
cat_adjacente = float(input('Comprimentento do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)

print('A hipotenusa dos catetos {} e {} é {:.2f}.'.format(cat_oposto, cat_adjacente, hipotenusa))
