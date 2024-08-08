"""
030
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

print('──── PARES OU ÍMPARES  ────')
numero = int(input('Escreva um número qualquer: '))
# calcula o resto da divisão por 2. se o resto for = 0, significa que o número é par; caso contrário, é ímpar
par = numero % 2
if par == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é IMPAR.'.format(numero))