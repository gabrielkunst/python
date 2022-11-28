"""  
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

from time import sleep
dic = {}
print('\033[1;32m-\033[m'*40)
print('\033[1;32m{:^40}\033[m' .format('INFORMAÇÕES'))
print('\033[1;32m-\033[m'*40)
name = str(input('Nome: ')).strip().title()
dic['name'] = name
while True:
    aver = float(input(f'Média do/a {dic["name"]}: '))
    if 60 <= aver <=100:
        sit = 'Aprovado'
        dic['sit'] = sit
        break
    elif 0 <= aver < 60:
        sit = 'Reprovado'
        dic['sit'] = sit
        break
    else:
        print('Média inválida, por favor digite um valor entre 0 e 100.')
dic['aver'] = aver
print('\033[1;32mGERANDO BOLETIM...\033[m')
sleep(3)
print()
print('\033[1;32m-\033[m'*40)
print('\033[1;32m{:^40}\033[m' .format('BOLETIM'))
print('\033[1;32m-\033[m'*40)
print(f'Nome = {dic["name"]}')
print(f'Média = {dic["aver"]}')
print(f'Situação = {dic["sit"]}')

