"""  
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""

import inquirer
teams = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Vasco', 'Brasil', 'Fortaleza', 'São Paulo','Alemanha', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Piauí', 'Avaí', 'Juventude')
list = ('Ver colocação', 'Ver os 5 primeiros colocados', 'Ver os 4 últimos colocados',
        'Ver os times em ordem alfabética', 'Ver a posição do meu time', 'Sair do programa')

while True:
    print('\n')
    questions = [
        inquirer.List('option',
                    message='O que você deseja fazer?',
                    choices=list,
                    ),
    ]
    
    answers = inquirer.prompt(questions)
    option = answers['option']

    if option == list[0]:
        print('A colocação foi:')
        for i in range(0, len(teams)):
            print(f'{i+1:2}) {teams[i]}')
    elif option == list[1]:
        print('Os 5 primeiros colocados foram:')
        for i in range(0, 5):
            print(f'{i+1:2}) {teams[i]}')
    elif option == list[2]:
        print('Os últimos 4 colocados foram:')
        for i in range(16,20):
            print(f'{i+1:2}) {teams[i]}')
    elif option == list[3]:
        print('A ordem dos times é:')
        for i in range(0, 20):
            print(f'{i+1:2}) {sorted(teams)[i]}')
    elif option == list[4]:
        while True:
            team = str(input('Qual é o seu time? ')).strip().title()
            try:
                print(
                    f'O {team.title()} ficou na posição {(teams.index(team))+1}')
                break
            except ValueError:
                print('Escreva o nome corretamente.')
    elif option == list[5]:
        print('Você escolheu SAIR.')
        break
