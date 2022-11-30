"""  
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

from time import sleep
dic = {}
goals = []

print('-'*40)
print('{:^40}' .format(' INFORMAÇÕES '))
print('-'*40)
dic['name'] = str(input('Nome: ')).strip().title()
games = int(input('Número de partidas: '))
for i in range(games):
    goals.append(int(input(f'Quantos goals {dic["name"]} fez no jogo {i+1}? ')))
    dic['goals'] = goals 
print()
sleep(2)
print('-'*40)
print('{:^40}' .format(' APROVEITAMENTO '))
print('-'*40)
print(f'{dic["name"]} jogou {games} partidas.')
for c, v in enumerate(dic['goals']):
    print(f'Na partida {c+1}, {dic["name"]} fez {dic["goals"][c]} goals!')
    sleep(1)
print(f'{dic["name"]} fez no total {sum(dic["goals"])} goals')
