"""
032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

print('-' * 45)
print('Vamos descobrir se um ano qualquer é bissexto?')
print('-' * 45)
ano = int(input('➔ ANO: '))

# um ano é bissexto se ele for divisível por 4, mas não por 100, ou se ele for divisível por 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))