"""
033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
n3 = int(input('Insira o 3º número: '))

# menor:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# maior:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número registrado foi {}, e o maior {}.'.format(menor, maior))
