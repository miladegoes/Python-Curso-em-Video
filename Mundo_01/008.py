"""
008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

# pede a entrada ao usuário
m = float(input('Insira uma medida qualquer em metros: '))

# realiza os calculos e armazena os resultados em variáveis
cm = m * 100
mm = m * 1000

# exibe os resultados
print('{}m em centímetros: {:.0f}cm'.format(m, cm))
print('{}m em milímetros: {:.0f}mm'.format(m, mm))
