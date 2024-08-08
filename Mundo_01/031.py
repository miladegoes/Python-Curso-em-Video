"""
031
Desenvolva um programa que pergunte a distância de uma viagem em Km.
- Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
- e R$0,45 para viagens mais longas.
"""

km_viagem = float(input('Insira a distância da viagem desejada: '))

if km_viagem > 200:
    print('O preço da sua viagem de {:.1f}Km será de R${:.2f}.'.format(km_viagem, km_viagem * 0.50))
else:
    print('O preço da sua viagem de {:.1f}Km será de R${:.2f}.'.format(km_viagem, km_viagem * 0.45))