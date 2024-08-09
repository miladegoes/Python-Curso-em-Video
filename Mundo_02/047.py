"""
047
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

# Cria uma sequência de 1 a 50:
for contagem in range(1, 51):
    if contagem  % 2 == 0: # lembrando que % retorna o resto de uma /. Números pares quando dividos por 2 retornam 0.
        print(contagem)