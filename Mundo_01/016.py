"""
016
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import trunc # importa a função truncate da biblioteca de matemática

numero = float(input('Digite um valor qualquer: '))
print(f'A porção inteira do valor {numero} é {trunc(numero)}.')