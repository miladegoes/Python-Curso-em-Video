"""
044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Bem-vinda ao Mercadinho PY. Insira o valor da compra: '))
print('=' * 50)
print('Opções de pagamento:')
print('[1] - À VISTA (5% de desconto)')
print('[2] - À VISTA NO CARTÃO (5% de desconto)')
print('[3] - 2X NO CARTAO')
print('[4] - 3X OU MAIS NO CARTÃO (20% de juros)')

escolha = int(input('Insira sua escolha: '))

if escolha == 1:
    print('Sua compra de R${:.2f} irá totalizar em R${:.2f}.'.format(valor, valor - (valor * 0.10)))
elif escolha == 2:
    print('Sua compra de R${:.2f} irá totalizar em R${:.2f}.'.format(valor, valor - (valor * 0.05)))
elif escolha == 3:
    print('Sua compra de R${:.2f} irá totalizar em R${:.2f}.'.format(valor, valor))
elif escolha == 4:
    escolha_parcela = int(input('Quantidade de parcelas: '))
    print('Sua compra de R${:.2f} será parcelada em {}X, totalizando em R${:.2f}.'.format(valor, escolha_parcela, valor + (valor * 0.20)))

print('=' * 50)

