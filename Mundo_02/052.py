"""
052
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

print('──────────────── NÚMEROS PRIMOS  ────────────────')

numero = int(input('Escreva um número inteiro qualquer: '))

# se menor que 2 não é primo
if numero < 2:
    print('O número {} não é primo.'.format(numero))
else:
# assume que o número é primo até que se prove o contrário
    primo = True

# verifica se o número é divisível por qualquer número de 2 até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break  # termina o loop se encontrar um divisor

    if primo:
        print('O número {} é primo.'.format(numero))
    else:
        print('O número {} não é primo.'.format(numero))