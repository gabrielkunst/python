"""  
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
#Função
def ficha(jogador='Desconhecido', goals=0):
    return print(f'O jogador {jogador} fez {goals} goal(s)!')

joga = str(input('Nome do jogador: ')).strip().title()
goal = str(input('Quantos goals: '))
if joga == '':
    joga = 'Desconhecido'
if goal.isnumeric():
    goals = goal
else:
    goal = 0
    

ficha(joga,goal)
