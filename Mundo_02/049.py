"""
049
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

numero = int(input('Escreva um número qualquer para gerar sua tabuada: '))
for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f'{numero} x {tabuada} = {resultado}')