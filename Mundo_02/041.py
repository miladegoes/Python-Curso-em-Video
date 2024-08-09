"""
41
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""

from datetime import date

data_atual = date.today().year #  date.today() retorna a data atual e .year extrai apenas o ano
data_nascimento = int(input('Data de nascimento do atleta: '))
idade = data_atual - data_nascimento

print('Idade do atleta: {}'.format(idade))

if idade <= 9:
    print('Esse atleta pertence a categoria MIRIM')
elif idade <= 14:
    print('Esse atleta pertence a categoria INFANTIL')
elif idade <= 19:
    print('Esse atleta pertence a categoria JÚNIOR')
elif idade <= 25:
    print('Esse atleta pertence a categoria SÊNIOR')
elif idade > 25:
    print('Esse atleta pertence a categoria MASTER')
