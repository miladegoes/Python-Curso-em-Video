"""
046
Faça um programa que mostre na tela uma contagem regressiva e mostre na tela
uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

import time

# define o número inicial da contagem:
inicio = 10

# inicio, parada, e passo negativo onde in range: o 1º argumento inicia, o 2º inclui o 0 na contagem,
# e o 3º é o passo negativo, que faz a contagem diminuir em 1 a cada iteração.
for contagem in range(inicio, -1, -1):
    print(contagem) # exibe a contagem regressiva com intervalo de 1 segundo entre cada iteração;
    time.sleep(1)

print("Feliz Ano Novo!!")
