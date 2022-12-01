"""  
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep
num = 0
def maior(*num):
    print('Analisando os valores passados...')
    print('Os valores informados foram: ', end='')
    for c, i in enumerate(num):
        num = list(num)
        print(num[c], end=' ', flush=True)
        sleep(0.5)  
    print()
    print(f'Foram informados {len(num)} valores.')
    print(f'O maior valor informado foi {max(num)}')
def linha():
    print()
    print('\033[1;32m-\033[m'*40)
    print()
linha()
maior(2,3,4,5)
sleep(0.5)
linha()
maior(42,45,2,32,52,62,12)
sleep(0.5)
linha()
maior(23,253,232,52,122,43)
sleep(0.5)
linha()
maior(1,2,3,4,5,6,7,8,9,9,10)
sleep(0.5)
linha()
maior(0)
linha()
