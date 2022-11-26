import inquirer
from time import sleep
count = 0
namlist = []
gradlist = []
while True:
    print('\033[1;32m-\033[m'*40)
    print('\033[1;32m{:^40}\033[m' .format(' MENU  '))
    print('\033[1;32m-\033[m'*40)
    opts = ['Adicionar alunos', 'Ver o boletim geral', 'Ver o boletim de um aluno específico', 'Sair do programa']
    questions = [
        inquirer.List('opt',
                    message='O que você deseja fazer?',
                    choices=opts,
                    ),
    ]
    chose = (inquirer.prompt(questions))['opt']
    if chose == opts[0]:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format(' ADICIONAR ALUNOS '))
        print('\033[1;32m-\033[m'*40)
        name = str(input('Nome: ')).strip().title()
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        aver = (n1 + n2)/2
        count += 1
        namlist.append(name)
        gradlist.append([n1, n2, aver])
    elif chose == opts[1]:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format(' BOLETIM GERAL '))
        print('\033[1;32m-\033[m'*40)
        if count == 0:
            print('Boletim \033[1;31mindisponível!\033[m')
            print('\033[1mAdicione\033[m alunos para poder ver o boletim.')
        else:
            print('{:<34}{:>6}' .format('NOME','MÉDIA'))
            for i in range(0, len(namlist)):       
                print(f'{namlist[i]:<34}{gradlist[i][2]:>6}')
    elif chose == opts[2]:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format(' BOLETIM ESPECÍFICO '))
        print('\033[1;32m-\033[m'*40)
        if count == 0:           
            print('Boletim \033[1;31mindisponível!\033[m')
            print('\033[1mAdicione\033[m alunos para poder ver o boletim.')
        else:
            name = input('Nome: ').strip().title()
            pos = int(namlist.index(name))
            print('\033[1;32m{:-^40}\033[m' .format(' BOLETIM '))
            print('{:<34}{:>6}' .format('NOME','MÉDIA'))
            n1 = gradlist[pos][0]
            n2 = gradlist[pos][1]
            aver = gradlist[pos][2]
            print(f'{name:<34}{aver:>6}')
    elif chose == opts[3]:
        print('\033[1;31m-\033[m'*40)
        print('\033[1;31m{:^40}\033[m' .format('SAIR'))
        print('\033[1;31m-\033[m'*40)
        print('Você escolheu \033[1;31mSAIR\033[m')
        print('Até mais... :(')
        sleep(3)
        break
    print()
    sleep(3)
