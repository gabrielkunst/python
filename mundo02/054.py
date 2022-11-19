"""  
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
countU = 0
countD = 0
for i in range(1,8):
    year = int(input(f'Em qual ano a pessoa {i} nasceu? '))
    age = (date.today().year - year)
    if age >= 18:
        countU =  countU + 1
    else:
        countD = countD + 1
if countU >= 2:
    print(f'{countU} pessoas são maiores de idade.', end=' ')

if countU == 1:
    print('1 pessoa é maior de idade.', end=' ')

if countD >= 2:
    print(f'{countD} pessoas são menores de idade.', end='')

if countD == 1:
    print('1 pessoa é menor de idade.', end=' ')

