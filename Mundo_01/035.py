"""
035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

print('△ CALCULANDO TRIÂNGULOS △')
r1 = float(input('1º medida: '))
r2 = float(input('2º medida: '))
r3 = float(input('3º medida: '))

# para formar um triangulo, a soma de dois lados tem que ser sempre menor que o terceiro lado
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas fornecidas formam um triângulo!')
else:
    print('As medidas fornecidas não podem formar um triângulo.')