"""
036
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
- Pergunte o valor da casa
- o salário do comprador e em quantos anos ele vai pagar.
- A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

print('Bem vindo(a) ao banco PY.')
print('Para aprovação de empréstimo, forneça alguns dados abaixo.')

valor_imovel = float(input('Valor do imóvel desejado: '))
salario_comprador = float(input('Sua renda mensal: '))
prazo_pgto = int(input('Em quantos anos deseja pagar: '))
prestacao = valor_imovel / (prazo_pgto * 12)

if prestacao <= salario_comprador * 0.30: # verifica se a prestação não excede 30% do salário
    print('Parabéns, seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo não foi aprovado.')
