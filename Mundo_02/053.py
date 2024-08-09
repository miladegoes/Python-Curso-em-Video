"""
053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

print('-= Detector de Palíndromos =-')
frase = str(input('Digite a frase desejada: ')).upper()
frase_formatada = frase.replace(" ", "") # elimina quaisquer espaços

# inicia as variáveis para verificação
tamanho = len(frase_formatada)
is_palindromo = True

for i in range(tamanho // 2): # itera pela metade da frase
    if frase_formatada[i] != frase_formatada[tamanho - 1 - i]: # compara o caractere atual com o correspondente no final da frase
        is_palindromo = False # se os caracteres forem diferentes, não é um palíndromo
        break # interrompe o laço

print('A frase {}:'.format(frase))
if is_palindromo:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

