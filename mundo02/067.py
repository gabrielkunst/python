from time import sleep
value = 0
count = 0
print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))
while True:
    print('\nDigite um número para ver sua tabuada.')
    value = int(input('Caso queira sair, digite um número negativo: '))
    if value < 0:
        print('Você escolheu SAIR! Até mais...')
        break
    while count < 10:
        count += 1
        print(f'{count:2} x {value:2} = {count*value:2}')
    count = 0
    
    sleep(0.5)

print('\033[1;32m{:-^40}\033[m' .format(' FIM '))