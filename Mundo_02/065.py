"""
065
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

print('Digite o número inteiro desejado.')

# inicia uma lista para armazenar os números inseridos
numeros = []

while True:
    numero = int(input('Número: '))
    numeros.append(numero)  # adiciona o número na lista

    # pergunta ao usuário se deseja adicionar mais números
    while True:
        mais_numeros = input('Deseja adicionar mais números? [S/N]: ').strip().upper()
        if mais_numeros == 'N':
            loop = False
            break
        elif mais_numeros == 'S':
            loop = True
            break
        else:
            print('Opção inválida, por favor tente novamente.')

    if not loop:  # sai do loop principal, verificando se loop é false
        break

# calcula a média, o maior e o menor valor
if numeros:
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    # resultados:
    print('A média dos valores digitados é: {:.1f}'.format(media))
    print('O maior valor digitado é: {}'.format(maior))
    print('O menor valor digitado é: {}'.format(menor))
else:
    print('Nenhum número foi digitado.')
