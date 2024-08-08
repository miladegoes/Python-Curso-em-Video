"""
026
Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra “A”,
- em que posição ela aparece a primeira vez
- e em que posição ela aparece a última vez.
"""

frase = str(input('Escreva uma frase qualquer: ')).strip().lower()
print('Na frase: {},'.format(frase))
print('A letra A aparece {} vezes;'.format(frase.count('a'))) # conta o número de ocorrências da letra 'a' na frase
# find retorna o índice da primeira ocorrência; + 1 ajusta para uma base 1, já que os índices em Python começam em 0
print('A letra A aparece pela primeira vez na posição {};'.format(frase.find('a')+1))
print('A letra A aparece pela última vez na posição {};'.format(frase.rfind('a')+1))
