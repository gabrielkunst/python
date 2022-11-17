"""  
1) Fazer um jogo de pedra, papel, tesoura.
"""
from random import choice
from time import sleep
print('\033[1;33m===\033[m'*20)
print('Olá, vamos jogar?')
print('Eu vou escolher entre \033[4mpedra, papel e tesoura\033[m. Vamos ver quem ganha.')
print('\033[1;33m===\033[m'*20)
list = ['pedra', 'papel', 'tesoura']
pc = choice(list)
user = str(input('Escolha entre pedra, papel ou tesoura:')).strip().lower()
sleep(3)
if pc == 'papel' and user == 'pedra':
    print('O sistema \033[1;32mganhou!\033[m')
    print(f'O sistema escolheu {pc}.')
elif pc == 'pedra' and user == 'tesoura':
    print('O sistema \033[1;32mganhou!\033[m')
    print(f'O sistema escolheu {pc}.')
elif pc == 'tesoura' and user == 'papel':
    print('O sistema \033[1;32mganhou!\033[m')
    print(f'O sistema escolheu {pc}.')
elif user == 'papel' and pc == 'pedra':
    print('O usuário \033[1;32mganhou!\033[m')
    print(f'O sistema escolheu {pc}.')
elif user == 'pedra' and pc == 'tesoura':
    print('O usuário \033[1;32mganhou!\033[m')
    print(f'O sistema escolheu {pc}.')
elif user == 'tesoura' and pc == 'papel':
    print('O usuário \033[1;32mganhou!\033[m')
    print(f'O sistema escolheu {pc}. ')
print('\033[1;33mBom jogo.\033[m Até mais!')


