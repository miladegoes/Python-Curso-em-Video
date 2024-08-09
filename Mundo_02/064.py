"""
064
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999).
"""

print('Bem vindo! Digite o número inteiro desejado ou 999 para sair do programa.')

# inicializa variáveis para contagem e soma
qnt_numeros = 0
soma_numeros = 0

while True:
    numero = int(input('Número: '))
    if numero == 999:
        break
    qnt_numeros += 1
    soma_numeros += numero

# exibe o resultado final
print('Você digitou {} números e a soma entre eles é {}.'.format(qnt_numeros, soma_numeros))
