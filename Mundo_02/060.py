"""
060
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
Programa para calcular o fatorial de um número usando o laço while
"""

numero = int(input("Digite um número qualquer para calcular seu fatorial: "))

# inicia as variáveis
fatorial = 1
contador = 1
sequencia = ""

# multiplica o valor atual de fatorial pelo valor de contador a cada iteração e constroi a sequência das multiplicações;
while contador <= numero:
    fatorial *= contador
    if contador == 1:
        sequencia += str(contador)
    else:
        sequencia += " x " + str(contador)
    contador += 1

print('{}! = {} = {}'.format(numero, sequencia, fatorial))

