"""
007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

# pede 2 notas do aluno e as armazena em variáveis individuais
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

# calcula a média somando as duas notas e dividindo pela quantidade de notas (2)
media = (n1 + n2) / 2

# exibe o resultado
print('As notas fornecidas são {:.1f} e {:.1f}. A média final do aluno é {:.1f}.'.format(n1, n2, media))
# {:.1f} - depois do ponto flutuante exibe apenas 1 digito
