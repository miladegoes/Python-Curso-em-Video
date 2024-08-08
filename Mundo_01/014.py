"""
14
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

print('-= CONVERSOR DE TEMPERATURA =-')
celcius = float(input('Insira a temperatura em °C: '))
fahrenheit = (celcius * 1.8) + 32

print('°C{:.1f} equivale a °F{:.1f}.'.format(celcius, fahrenheit))