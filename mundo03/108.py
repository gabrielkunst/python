"""  
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
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
print(f'Aumentando 25% de {uteis.moeda(n)}, temos {uteis.moeda(uteis.aum(n, 25))}')
print(f'Diminuindo 38% de {uteis.moeda(n)}, temos {uteis.moeda(uteis.dim(n, 38))}')
print(f'O dobro de {uteis.moeda(n)} é {uteis.moeda(uteis.dob(n))}')
print(f'A metade de {uteis.moeda(n)} é {uteis.moeda(uteis.met(n))}')
print('\033[1;31mSAINDO...\033[m')
sleep(2)
uteis.linha()
