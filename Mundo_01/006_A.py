"""
006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# método mais curto, usando f strings como exemplo;

# pede a entrada ao usuário
numero = int(input('Insira um número qualquer: '))

# imprime o resultado, já calculando sem utilizar variáveis
print(f'O dobro de {numero} é {numero * 2}.')
print(f'O triplo de {numero} é {numero * 3}.')
print(f'A raiz quadrada de {numero} é {numero ** (1/2):.2f}.')