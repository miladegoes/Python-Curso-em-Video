"""
043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

peso = float(input('Peso em KG: '))
altura = float(input('Altura em M: '))
imc = peso / (altura ** 2)

print(f'O IMC dos dados fornecidos é de {imc:.2f}.')

if imc < 18.5:
    print('Classificação: Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Classificação: Peso ideal')
elif imc >= 25 and imc < 30:
    print('Classificação: Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Classificação: Obeso')
elif imc > 40:
    print('Classificação: Morbidamente Obeso')