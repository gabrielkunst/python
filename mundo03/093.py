from time import sleep
dic = {}
list = []
nome = str(input('Nome: ')).strip().title()
totpart = int(input(f'Quantas partidas {nome} jogou?'))
totgoals = 0
for i in range(0, totpart):
    goals = int(input(f'Quantos goals {nome} fez no jogo {i+1}?'))
    totgoals += goals
    list.append(goals)
dic['Nome'] = nome
dic['Goals'] = list
dic['Total'] = totgoals
print()
print('-'*40)
print('{:^40}' .format(' APROVEITAMENTO '))
print('-'*40)
print(f'O {dic["Nome"]} jogou {totpart} partidas.')
for i in range(totpart):
    print(f'O {dic["Nome"]} fez {dic["Goals"][i]} goals na partida {i+1}!')
    sleep(1)
print(f'O {dic["Nome"]} fez no total, {dic["Total"]} goals ')

