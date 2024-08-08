"""
011
Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

largura = float(input('Largura: '))
altura = float(input('Altura: '))

area = largura * altura
qnt_tinta = area / 2

print('A área de {:.1f}m x {:.1f}m é {:.1f}m², e serão necessários {:.1f}L de tinta para pintá-la.'.format(largura, altura, area, qnt_tinta))