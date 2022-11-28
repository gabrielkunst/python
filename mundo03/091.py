from time import sleep
from random import randint

dic = {}
list = []
while True:
    print('-'*40)
    print('{:^40}' .format('JOGADOR DE DADOS'))
    print('-'*40)
    for i in range(4):
        name = str(input('Quem irá jogar o dado? ')).strip().title()
        print(f'{name} está jogando...')
        num = randint(0,6)
        dic['name'] = name
        dic['num'] = num
        list.append(dic.copy())
        sleep(2)
        print(f'{name} jogou {num}!')
        sleep(2)
        print()
    print('-'*40)
    print('{:^40}' .format('RANKING'))
    print('-'*40)
    print('{:<26}{:>4}' .format('NOME','JOGADA'))
    for c, i in enumerate(range(0, len(list))):
        list = sorted(list, key=lambda x:x['num'], reverse=True)
        print(f'{c+1}) {list[i]["name"]:<26}{list[i]["num"]:>3}')
    print()
    sleep(2)
    print('-'*40)
    print('{:^40}' .format(' MENU '))
    print('-'*40)
    while True:
        opt = str(input('Deseja jogar mais uma vez? [S/N] ')).strip().upper()
        if opt in 'SIM':
            break
        elif opt in 'NÃO':
            break
        else:
            print('Comando inválido, tente novamente.')
    print()
    list.clear()
    if opt in 'NÃO':
        print('Até mais...')
        sleep(2)
        break

print(dic)