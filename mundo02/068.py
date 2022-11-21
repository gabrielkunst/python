from random import randint
from time import sleep
count = 0

print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))
while True:
    num = int(input('\nDigite um valor: '))
    user = int(input('''Par ou ímpar? 
[1] PAR
[2] ÍMPAR
Escolha um número: '''))
    sleep(1)
    pc = (randint(0,100))
    sum = (num + pc)
    if sum%2 == 0:
        if user == 1:
            count += 1
            print('Você ganhou!')
            print(f'Os números escolhidos foram {num} e {pc} sendo a soma deles, {num+pc}, PAR!')
        elif user == 2:
            print('Você perdeu!')
            print(f'Os números escolhidos foram {num} e {pc} sendo a soma deles, {num+pc}, PAR!')
            break
        else: 
            print('Digite um número válido!')
    else:
        if user == 1:
            print('Você perdeu!')
            print(f'Os números escolhidos foram {num} e {pc} sendo a soma deles, {num+pc}, ÍMPAR!')
            break
        elif user == 2:
            count += 1
            print('Você ganhou!')
            print(f'Os números escolhidos foram {num} e {pc} sendo a soma deles, {num+pc}, ÍMPAR!')
        else:
            print('Digite um número válido!')
if count > 0:
    print(f'Você ganhou {count} vezes. Parabéns!')
else: 
    print('Você não ganhou nenhuma vez, tente novamente.')
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))