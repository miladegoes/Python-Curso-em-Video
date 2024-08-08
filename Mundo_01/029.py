"""
029
Escreva um programa que leia a velocidade de um carro.
- Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
- A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = float(input('Velocidade do veículo registrada pelo radar: '))
multa = velocidade - 80

if velocidade > 80:
    print('''A velocidade desse veículo ultrapassou o limite permitido de 80Km/0.
Valor da multa: R${:.2f}'''.format(multa * 7))
else:
    print('Esse veículo não ultrapassou o limite de velocidade de 80Km/0, portanto não será multado.')

print('-' * 32)
print('Não corra, não mate, não morra.')
print('-' * 32)