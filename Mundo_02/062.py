"""
062
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
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

# pergunta quantos termos adicionais ele quer mostrar, e continua perguntando até que o usuario digite 0
while True:
    mais_termos = int(input('Quantos termos a mais você quer mostrar? (0 para encerrar): '))
    if mais_termos == 0:
        break
    for i in range(mais_termos):
        print('Termo {}: {}'.format(contador + 1, termo))
        termo += razao
        contador += 1

print('PA encerrada.')
