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
print(dic)