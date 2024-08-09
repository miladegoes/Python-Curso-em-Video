"""
048
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0 # armazena a soma dos múltiplos de 3;
quantidade = 0 # armazena o total de números múltiplos de 3;

for numeros in range(1, 501): # itera o intervalo de 1 a 500;
    if numeros % 3 == 0: # identifica os números múltiplos de 3;
        soma += numeros # adiciona o valor de numeros à variável soma se a condição do if for verdadeira.
        quantidade += 1 # além de somar o número múltiplo de 3 à variável soma, incrementa o contador em 1 para cada número que for múltiplo de 3.

print('Entre 1 e 500 existem {} números múltiplos de 3.'.format(quantidade))
print('A soma entre todos esses números é de {}.'.format(soma))
