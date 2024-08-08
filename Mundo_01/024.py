"""
# 024
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

cidade = str(input('Digite o nome de uma cidade: ')).strip().lower().capitalize()
print('Essa cidade começa com Santo? ➔ {}'.format('Santo' in cidade[:5]))

# cidade[:5] pega os primeiros 5 caracteres da string cidade
# 'Santo' in cidade[:5] verifica se a substring 'Santo' está presente nos primeiros 5 caracteres da string cidade.
# o operador in retorna true se a substring for encontrada, e false caso contrário.