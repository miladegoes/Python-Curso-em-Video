"""
037
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
numero = int(input('Digite um número inteiro qualquer: '))
print("Agora, escolha a base de conversão:")
print("[1] - Binário")
print("[2] - Octal")
print("[3] - Hexadecimal")
opcao = int(input("Sua escolha: "))

# retorna uma string com '0b' no início, por isso [2:] para remover-la
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('Dado inválido, tente novamente.')
