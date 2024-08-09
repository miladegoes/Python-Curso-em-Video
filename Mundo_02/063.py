"""
063
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""

print('-= SEQUÊNCIA DE FIBONACCI =-')
n = int(input('Quantidade de termos que deseja exibir: '))

# inicializa os dois primeiros termos do fibonacci, sempre sendo 0 e 1
a, b = 0, 1
contador = 0

# armazena sequência formatada
resultado = ''

while contador < n:
    if contador == 0:
        resultado += str(a)
    else:
        resultado += ' – ' + str(a)
    a, b = b, a + b
    contador += 1

print(resultado)
