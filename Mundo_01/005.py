"""
005
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

# pede um número inteiro ao usuário
numero = int(input('Insira um número qualquer: '))

# armazena o número antecessor e sucessor em variáveis
antecessor = numero - 1
sucessor = numero + 1

# imprime o resultado
print('O antecessor do número {} é {} e seu sucessor é {}.'.format(numero, antecessor, sucessor))


