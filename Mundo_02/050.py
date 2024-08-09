"""
050
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))
n4 = int(input('Escreva o quarto número: '))
n5 = int(input('Escreva o quinto número: '))
n6 = int(input('Escreva o sexto número: '))

lista = [n1, n2, n3, n4, n5, n6] # organiza os números numa lista

soma_pares = 0 # inicializa a  variável que  vai armazenar a soma dos pares

for numeros in lista: # itera sobre cada número da lista
    if numeros % 2 == 0: # verifica se é par
        soma_pares += numeros # adiciona o número par a soma

print('A soma entre os números PARES fornecidos é de {}'.format(soma_pares))