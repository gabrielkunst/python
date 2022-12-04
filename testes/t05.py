import inquirer
from time import sleep  

tot = []
temp = []
count = 0
while True:
    print('\033[1;32m-\033[m'*40)
    print('\033[1;32m{:^40}\033[m' .format(' MENU ') )
    print('\033[1;32m-\033[m'*40)
    list = ['Adicinar uma pessoa','Mostrar banco de dados','Sair do programa']
    questions = [
        inquirer.List('opt',
                    message='O que deseja fazer?',
                    choices=list,
                    ),
    ]
    chose = (inquirer.prompt(questions))['opt']
    if chose == list[0]:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format(' ADICIONAR USUÁRIO '))
        print('\033[1;32m-\033[m'*40)
        name = str(input('Digite o nome: ')).strip()
        while True:
            age = int(input('Digite a idade: '))
            if age < 0:
                print('Tente novamente :(')
            else:
                break
        temp = [name, age]
        tot.append(temp[:])
        temp.clear()
        print('\033[1;32mADICIONANDO...\033[m')
        sleep(1)
        print('\033[1;32mUSUÁRIO ADICIONADO COM SUCESSO!\033[m')
        count += 1
        sleep(2)
        print()
    elif chose == list[1]:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format(' BANCO DE DADOS '))
        print('\033[1;32m-\033[m'*40)
        if tot != []:
            print('{:<34}{:^6}' .format('NOMES','IDADES'))
            for i in range(0, len(tot)):
                print(f'{tot[i][0].title():<34}{tot[i][1]:^6}')
            count += 1
            sleep(3)
        else:
            print('\033[1;31mErro!\033[m Banco de dados indisponível no momento...')
            print('Cadastre um usuário para que o banco de dados esteja disponível.')
            sleep(3)
            print('\033[1;32mLEVANDO VOCÊ DE VOLTA AO MENU...\033[m')
        sleep(2)
        print()
    elif chose == list[2]:
        print('\033[1;31m-\033[m'*40)
        print('\033[1;31m{:^40}\033[m' .format('SAIR'))
        print('\033[1;31m-\033[m'*40)
        print('Você escolheu \033[1;31mSAIR\033[m')
        print('\033[1;31mSAINDO...\033[m')
        sleep(2)
        break

