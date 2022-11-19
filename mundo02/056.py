"""  
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
agesum = 0
olderman = 0 
oldermans_name = ''
womanlesstwenty = 0

for i in range(1,5):
    print('\033[1;33m{:-^40}\033[m' .format(f' {i}ª PESSOA '))
    name = str(input('Nome: ')).strip().lower()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().lower()
    agesum += age
    ageav = (agesum/i)
    if i == 1 and sex == 'm':
        olderman = age
        oldermans_name = name
    if age > olderman and sex == 'm':
        olderman = age
        oldermans_name = name
    if age < 20 and sex == 'f':
        womanlesstwenty += 1
    else:
        print('Não há mulheres com mais de 20 anos nesse grupo.')


print(f'A média das idades é {ageav}.')
print(f'O homem mais velho tem {olderman} anos e seu nome é {oldermans_name.title()}.')
print(f'Há nesse grupo {womanlesstwenty} mulheres com menos de 20 anos.')
