"""
015
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print('----------------------------------------------------')
print('Olá! Seja bem-vindo ao Py Aluguel de veículos.')
print('Alugou conosco? Por favor, preencha os dados abaixo.')
print('----------------------------------------------------')

km_percorrido = float(input('Km percorrido: '))
qnt_dias = int(input('Período de posse em dias: '))
valor = (qnt_dias * 60) + (km_percorrido * 0.15)

print('Você percorreu {:.1f}Km num período de {} dia(s). O valor do aluguel totalizou em R${:.2f}.'.format(km_percorrido, qnt_dias, valor))