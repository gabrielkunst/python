"""  
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 
"""

from random import randint
from time import sleep
list = []
guess = int(input('Quantos palpites você deseja gerar? '))
for i in range(guess):
    print('\033[1;32m{:-^40}\033[m' .format(f' {i+1}° PALPITE '))
    temp = []
    wid = len(temp)
    while len(temp) != 6:
        num = randint(1,60)
        if num in temp:
            pass
        else:
            chose = (f'O {wid+1}° número sorteado será: {num}')
            print(chose)
            temp.append(num)
            temp.sort()
            wid = len(temp)
    list.append(temp[:])
    sleep(1)
print('\n')
print('A lista formada por todos os palpites gerados é:')
for i in range(0, guess):
    print(list[i])
    