from random import randint
from time import sleep
num = []
tot = 0
def sortear():
    for i in range(5):
        num.append(randint(0,10))
    print(f'Os números sorteados são: ', end='')
    for c, i in enumerate(num):
        print(num[c], flush=True, end=' ')
        sleep(0.5)
def somar():
    print()
    tot = 0
    for c, i in enumerate(num):
        if num[c] % 2 == 0:
            tot += num[c]
    print(f'Somando os números pares de {num}, temos {tot}')  
def linha():
    print()
    print('\033[1;32m-\033[m'*40)
    print()
linha()
sortear()
somar()
linha()