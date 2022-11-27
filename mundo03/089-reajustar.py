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
print('{:<36}{:>4}' .format('NOME','MÉDIA'))
for c, i in enumerate(range(0, len(list))):
    print(f'{c}){list[i][0]:<36}{list[i][2]:<4}')
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