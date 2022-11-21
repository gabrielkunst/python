"""  
1) Fazer um programa que jogue JOKENPÔ com o usuário.
"""
#módulos
from random import choice
from time import sleep
import inquirer


print('\033[1;32m{:=^40}\033[m' .format(' Vamos Jogar? '))
#menu para selecionar a jogada
list = ['Pedra', 'Papel', 'Tesoura']
questions = [
    inquirer.List('options',
        message='Qual será sua jogada?',
        choices= list,
        ),
]
answers = inquirer.prompt(questions)
user = str((answers['options'])).lower()
pc = str(choice(list)).lower()


#timer
print('\033[1;33mJO\033[m')
sleep(0.5)
print('\033[1;33mKE\033[m')
sleep(0.5)
print('\033[1;33mPÔ!!!\033[m')
sleep(0.25)
print('\033[1;36m{:=^40}\033[m' .format(' RESULTADO '))


#condições
if pc == 'pedra' and user == 'pedra':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;33mEMPATE!\033[m')
elif pc == 'papel' and user == 'papel':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;33mEMPATE!\033[m')
elif pc == 'tesoura' and user == 'tesoura':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;33mEMPATE!\033[m')
elif pc == 'papel' and user == 'pedra':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;31mPC! Você PERDEU!\033[m')
elif pc == 'papel' and user == 'tesoura':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;32mUSER! Você GANHOU!\033[m')
elif pc == 'pedra' and user == 'papel':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;32mUSER! Você GANHOU!\033[m')
elif pc == 'pedra' and user == 'tesoura':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;31mPC! Você PERDEU!\033[m')
elif pc == 'tesoura' and user == 'papel':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;31mPC! Você PERDEU!\033[m')
elif pc == 'tesoura' and user == 'pedra':
    print(f'Escolha do usuário: {user}.')
    print(f'Escolha do computador: {pc}.')
    print('\033[1;32mUSER! Você GANHOU!\033[m')
else:
    print('Erro. Tente novamente.')
    
print('Até mais <3!')




