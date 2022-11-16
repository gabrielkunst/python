"""  
1) O programa deve escolher um número aleatório entre 0 e 1000
2) Deve haver um input para que o usuário tente acertar tal número
3) Retorne por meio de uma condição se o usuário acertou ou não o número.
"""
from random import randint
from time import sleep
print('==='*20)
print('Vou pensar em um número entre 0 e 1000, tente acertar.')
print('==='*20)
numpc = randint(0,1001) #Deve se colocar (início, fim+1)
numuser = int(input('Digite um número:'))
print('\033[1;32mCARREGANDO...\033[m')
sleep(3)
if numuser == numpc:    
    print(f'\033[1;33mCORRETO!\033[m O número escolhido foi \033[4m{numpc}\033[m].')
else:
    print(f'\033[1;31mERRADO!\033[m O número escolhido foi \033[4m{numpc}\033[m!')