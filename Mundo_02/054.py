"""
054
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

# inicializa variáveis para contar quantas pessoas são maiores de idade e quantas não são.
maior = 0
menor = 0

ano_atual = date.today().year

for i in range (1, 8): # define a iteração de 1 a 7)
    ano_nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(i)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Dentre essas pessoas, {} são maiores de idade e {} são menores de idade.'.format(maior, menor))

