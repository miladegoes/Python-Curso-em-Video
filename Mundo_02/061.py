"""061
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('PROGRESSÃO ARITMÉTICA')
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

# inicializa o contador e o termo
contador = 0
termo = primeiro_termo

# calcula e exibe os 10 primeiros termos usando while
while contador < 10:
    print('Termo {}: {}'.format(contador + 1, termo))
    termo += razao
    contador += 1
