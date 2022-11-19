"""  
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 
"""
from time import sleep
start = (input('Digite 0 para iniciar o programa: '))
if start == '0':
    print('Os números \033[1;32mpares\033[m no intervalo de 1 - 50 são:')
    sleep(1)
    for x in range(2,51,2):
        print(x, end=', ')
else:
    print('Comando inválido! Tente novamente.')