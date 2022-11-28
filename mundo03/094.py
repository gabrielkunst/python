"""  
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
"""

dict = {}
list = []
totage = 0
woman_list = []
older_list = []
print('-'*40)
print('{:^40}' .format(' INÍCIO '))
print('-'*40)
while True:
    name = str(input('Nome: ')).strip().title()
    age = int(input('Idade: '))
    while True: 
        sex = str(input('Sexo: [M/F] ')).strip().upper()
        if sex == 'M':
            break
        elif sex == 'F':
            break
        else:
            print('Escolha uma opção válida.')
    dict['name'] = name
    dict['age'] = age
    dict['sex'] = sex
    list.append(dict.copy())
    dict.clear()

    while True:
        opt = str(input('Deseja adicionar mais uma pessoa? [S/N] ')).strip().upper()
        if opt == 'S': 
            break
        elif opt == 'N':
            break
        else:
            print('Comando inválido, tente novamente.')
    if opt == 'N':
        break
print()
print('-'*40)
print('{:^40}' .format('INFORMAÇÕES'))
print('-'*40)
print(f'Foram cadastradas {len(list)} pessoas.')
for i in range(0, len(list)):
    age = list[i]['age']
    sex = list[i]['sex']
    if sex == 'F':
        woman_list.append(list[i]['name'])
    totage += age
aver = totage/len(list)
print(f'A média de idade do grupo é: {aver}')
if len(woman_list) == 0:
    print('Não há mulheres cadastradas.')
else: 
    print(f'Há {len(woman_list)} mulheres cadastradas, são elas: {woman_list}')
for i in range(0, len(list)):
    age = list[i]['age']
    if age > aver:
        older_list.append(list[i]['name'])
if len(older_list) == 0:
    print('Não há pessoas maiores da média.')
else:
    print(f'Há {len(older_list)} pessoas acima da média, são elas: {older_list}')
print()
print(dict)

