"""
051
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

print('PROGREÇÃO ARITMÉTICA')
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

# calcula e exibe os 10 primeiros termos
for i in range(10):
    termo = primeiro_termo + i * razao
    print('Termo {}: {}'.format(i + 1, termo))
