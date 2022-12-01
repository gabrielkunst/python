"""  
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
"""
from time import sleep
def contador(a,b,c):
    if c < 0:
        c *= -1
    if c == 0:
        c == 1
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    
    if a < b:
        count = a
        while count <= b:
            print(f'{count}', end=' ', flush=True)
            count += c
            sleep(0.5)
        print()
    else:
        count = a
        while count >= b:
            print(f'{count}', end=' ', flush=True)
            count -= c
            sleep(0.5)
        print()

def linha():
    print()
    print('\033[1;32m-\033[m'*40)
    print()

linha()
contador(1,10,1)
linha()
contador(10,0,2)
linha()
print('Agora é sua vez!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
linha()
contador(a,b,c)
linha()