from time import sleep
dict = {}
all = []
list = []
totgoals = 0
while True:
    print('-'*40)
    print('{:^40}' .format('ADICIONAR JOGADOR'))
    print('-'*40)
    list = []
    name = str(input('Nome: ')).strip().title()
    games = int(input('Número de partidas: '))
    for i in range(0, games):
        goals = int(input(f'Quantos goals o {name} fez no jogo {i+1}?'))
        list.append(goals)
        totgoals += goals
    dict['name'] = name
    dict['totgames'] = games
    dict['totgoals'] = totgoals
    dict['goals'] = list
    all.append(dict.copy())
    
    print()
    sleep(1)
    print('-'*40)
    print('{:^40}' .format('MENU'))
    print('-'*40)
    while True:
        opt = int(input('''O você deseja fazer:
    [1] Adicionar mais um jogador
    [2] Ver aproveitamentos
    [3] Sair do programa
    Escolha um número: '''))
        if opt == 1:
            break
        elif opt == 2:
            print('-'*40)
            print('{:^40}' .format('APROVEITAMENTO'))
            print('-'*40)
            print('{:<2}{:^8}{:<10}{:<10}' .format('NÚM', 'NOME', 'GOALS', 'TOTAL'))
            for x in range(0, len(all)):
                print(f'{(i):<2}) {(all[x]["name"]):^7}{(all[x]["goals"])}{(all[x]["totgoals"]):<10}')
        elif opt == 3:
            break
        else:
            print('Comando inválido, tente novamente.')
    print()
    if opt == 3:
        print('SAINDO...')
        sleep(3)
        break
    