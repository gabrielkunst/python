"""  
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
option = int(input('Digite 0 para iniciar o programa: '))
if option == 0:
    for x in range(10, -1, -1):
        print(f'\033[1;31m{x}\033[m')
        sleep(0.5)
    print('\033[1;32mFELIZ ANO NOVO!!!\033[m')
else: 
    print('Opção inválida! Tente novamente.')