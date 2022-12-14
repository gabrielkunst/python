"""  
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from time import sleep
list = []
while True:
    name = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aver = (n1+n2)/2
    list.append([name, [n1, n2], aver])
    while True:
        opt = str(input('Deseja adicionar mais um aluno? [S/N] ')).strip().upper()
        if opt == 'S':
            break
        elif opt == 'N':
            break
        else: 
            print('Comando inválido, tente novamente.')
    if opt == 'N':
        break
sleep(2)
print()
print('\033[1;32m-\033[m'*40)
print('\033[1;32m{:^40}\033[m' .format(' BOLETIM '))
print('\033[1;32m-\033[m'*40)
print('{:<34}{:>6}' .format('NOME','MÉDIA'))
for c, i in enumerate(range(0, len(list))):
    print(f'{c}) {list[i][0]:<31}{list[i][2]:>6}')
sleep(3)
while True:    
    num = int(input('Para ver as notas de um aluno, digite o seu respectivo número: (999 para sair) '))
    if num == 999:
        print('SAINDO...')
        sleep(2)
        break
    elif 0 <= num <= len(list):
        for i in range(0, len(list)):
            if num == i:
                print(f'{list[i][0]} ---> {list[i][1]}')
                print()
    else:
        print('Comando inválido! Tente novamente.')
        print()



"""  
AJUSTES:
COLOCAR NOME E MÉDIA DE FORMA TABULAR!

"""