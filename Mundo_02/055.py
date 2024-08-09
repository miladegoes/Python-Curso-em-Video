# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = float(input('Peso da 1ª pessoa: ')) # define peso da 1 pessoa para ter referência inicial

for i in range(2, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso registrado foi de {}kg, e o menor {}kg.'.format(maior, menor))
