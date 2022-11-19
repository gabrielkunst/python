"""  
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
"""
from time import sleep
num = int(input('Digite um valor inteiro: '))
tot = 0
sleep(1)
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else: 
        print('\033[1;31m' , end='')
    print(c, end=' ')
if tot == 2:
    print(f'\n\033[mO número {num} \033[1;32mÉ PRIMO,\033[m pois possui {tot} divisores.')
else: 
    print(f'\n\033[mO número {num} \033[1;31mNÃO É PRIMO,\033[m pois possui {tot} divisores.')
