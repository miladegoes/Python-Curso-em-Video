"""
006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# pede a entrada ao usuário
numero = int(input('Insira um número qualquer: '))

# armazena o resultado do dobro, triplo e raiz quadrada em variáveis
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print('Número inserido: {}'.format(numero))
print('O dobro de {} é {}.'.format(numero, dobro))
print('O triplo de {} é {}.'.format(numero, triplo))
print('A raiz quadrada de {} é {:.2f}.'.format(numero, raiz))
# {:.2f} - depois do ponto flutuante exibe apenas 2 digitos
