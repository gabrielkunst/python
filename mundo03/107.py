"""  
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import uteis
from time import sleep
n = 0
uteis.linha()
while True: 
    try:
        n = int(input('Digite um valor: R$ '))
        type(n) == 'int'
        break
    except ValueError:
        print('ERRO! Digite um valor válido!')
print('\033[1;32mAGUARDE...\033[m')
sleep(2)
uteis.aumentar(n,35)
uteis.diminuir(n,50)
uteis.dobro(n)
uteis.metade(n)
print('\033[1;31mSAINDO...\033[m')
sleep(2)
uteis.linha()
