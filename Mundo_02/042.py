"""
042
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""

print('△ CALCULANDO TRIÂNGULOS △')
r1 = float(input('1º medida: '))
r2 = float(input('2º medida: '))
r3 = float(input('3º medida: '))

# para formar um triângulo, a soma de dois lados tem que ser sempre maior que o terceiro lado
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas fornecidas formam um triângulo!')
    if r1 == r2 and r2 == r3:
       print('O triângulo formado é um EQUILÁTERO, pois tem todos os lados iguais.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo formado é um ISÓSCELES, pois tem dois lados iguais e um diferente.')
    else:
        print('O triângulo formado é um ESCALENO, pois tem todos os lados diferentes.')
else:
    print('As medidas fornecidas não podem formar um triângulo.')
