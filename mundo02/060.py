from math import factorial
from time import sleep

n = int(input('\nDigite um valor: '))
op = ''
while op != 3:
    print('\n\033[1;32m{:-^40}\033[m'.format(' INÍCIO '))
    
    op = int(input('''\nO que você deseja fazer? 
[1] Fatorial
[2] Escolher um novo número
[3] Sair do programa
Escolha um número: '''))
    sleep(1)

    if op == 1:
        fat = factorial(n)
        print('\nVocê escolheu FATORIAL.')
        print(f'O fatorial de {n} é {fat}.')
    elif op == 2:
        print('\nVocê escolheu NOVO NÚMERO.')
        n = int(input('Digite um valor: '))
    elif op == 3:
        print('\nVocê escolheu SAIR DO PROGRAMA.')
        print('Até mais.')
    else: 
        print('Escolha um número válido!')
    sleep(0.5)
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))