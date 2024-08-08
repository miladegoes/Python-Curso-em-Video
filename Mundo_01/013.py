"""
013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input('Insira o salário do colaborador: R$ '))
novo_salario = salario + (salario * 0.15)

print('Esse funcionário recebeu 15% de aumento, e passará a receber R${:.2f}.'.format(novo_salario))
