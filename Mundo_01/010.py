"""
010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

print('A cotação do dolar hoje é R$4,90.')

# pede a entrada ao usuário
carteira = float(input('Insira a quantia em Reais para realizar a conversão: R$'))

# exibe o resultado e o calculo de conversão
print(f'R${carteira:.2f} equivalem a ${carteira / 4.90:.2f}.')
