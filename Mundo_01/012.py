"""
012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

valor = float(input('Insira o valor do produto a seguir: R$'))
desconto = valor - (valor * 0.05)
print('O valor do produto é R${:.2f} e com 5% de desconto, R${:.2f}.'.format(valor, desconto))
