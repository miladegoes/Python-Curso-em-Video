"""
039
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora exata de se alistar
- se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date # a clase date é usada para trabalhar com datas

print('=' * 20)
print('ALISTAMENTO MILITAR')
print('=' * 20)

data_atual = date.today().year #  date.today() retorna a data atual e .year extrai apenas o ano
data_nascimento = int(input('Ano de nascimento: '))
idade = data_atual - data_nascimento

print('Você nasceu em {} e tem {} anos, portanto: '.format(data_nascimento, idade))

if idade < 18:
    print('Você ainda não completou 18 anos e poderá se alistar apenas daqui {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você está no momento exato para se alistar, bora soldado!')
elif idade > 18 and idade < 45:
    print('Você já deveria ter se alistado há {} anos, mas ainda dá tempo!'.format(idade - 18))
elif idade >= 45:
    print('Você já passou da idade máxima para o alistamento, que é de 45 anos.')
