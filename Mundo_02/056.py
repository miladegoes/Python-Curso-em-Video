"""
056
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- a média de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres têm menos de 20 anos
"""

# listas para armazenar as informações de cada pessoa
nomes = []
idades = []
sexos = []

for i in range(1, 5):
    print('Informações da {}ª pessoa:'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()

# adiciona as informações às listas
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

# inicia variáveis para os cálculos
total_idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(4):
    total_idade += idades[i]

    if sexos[i] == 'M' and idades[i] > idade_homem_mais_velho:
        idade_homem_mais_velho = idades[i]
        homem_mais_velho = nomes[i]

    if sexos[i] == 'F' and idades[i] < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / 4 # calcula a média de idade

print("\nInformações das 4 pessoas:")
for i in range(4):
    print("Nome: {}, Idade: {}, Sexo: {}".format(nomes[i], idades[i], sexos[i]))

print("\nA média de idade do grupo é: {:.2f} anos.".format(media_idade))
if homem_mais_velho:
    print("O homem mais velho é {}, com {} anos.".format(homem_mais_velho, idade_homem_mais_velho))
else:
    print("Não há homens no grupo.")
print("Há {} mulher(es) com menos de 20 anos.".format(mulheres_menos_20))
