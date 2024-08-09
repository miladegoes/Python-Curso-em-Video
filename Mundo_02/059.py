"""
059
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

print('Forneça dois números que você deseja calcular.')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0

while opcao != 5:
    print('''\nOpções:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Opção desejada: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif opcao == 4:
        print('Forneça dois novos números:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Programa finalizado.')
    else:
        print('Opção inválida. Tente novamente.')
