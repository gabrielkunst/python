from random import randint
from time import sleep
list = []
guess = int(input('Quantos palpites você deseja gerar? '))
for i in range(guess):
    print('\033[1;32m{:-^40}\033[m' .format(f' {i+1}° PALPITE '))
    temp = []
    for i in range(0, 6):
        num = randint(1,60)
        while True:
            #### SE LEN(TEMP) < 6, CONTINUAR A GERAR RANDOM NUMBERS, ELSE: BREAK
            if num in temp:
                pass
            else: 
                temp.append(num)
        chose = (f'O {i+1}° número sorteado será: {num}')
        print(chose)
        temp.sort()
    list.append(temp[:])
    del temp
    sleep(1)
print('\n')
print('A lista formada por todos os palpites gerados é:')
for x in range(0, guess):
    print(list[x])
    