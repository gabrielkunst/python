"""  
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

import uteis
from time import sleep
n = 0
uteis.linha()
while True: 
    try:
        n = float(input('Digite um valor: R$ '))
        type(n) == 'float'
        break
    except ValueError:
        print('ERRO! Digite um valor válido!')
print('\033[1;32mAGUARDE...\033[m')
sleep(2)
print(f'Aumentando 25% de {uteis.moeda(n)}, temos {uteis.aum(n, 25, True)}')
print(f'Diminuindo 38% de {uteis.moeda(n)}, temos {uteis.dim(n, 38, True)}')
print(f'O dobro de {uteis.moeda(n)} é {uteis.dob(n, True)}')
print(f'A metade de {uteis.moeda(n)} é {uteis.met(n, True)}')
print('\033[1;31mSAINDO...\033[m')
sleep(2)
uteis.linha()
