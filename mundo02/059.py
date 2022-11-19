from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
big = 0
op = 0
sleep(1)
while op != 5:
    print('\n\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))
    op = int(input('''\nO que você deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos números
[5] Sair do programa
Escolha um número: '''))

    sleep(1)
    if op == 1:
        print('\nVocê escolheu SOMAR')
        print(f'A soma entre {n1} e {n2} é {n1+n2}.')
    elif op == 2:
        print('\nVocê escolheu MULTIPLICAR')
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}.')
    elif op == 3:
        print('\nVocê escolheu MAIOR NÚMERO')
        if n1 > n2:
            print(f'O maior número é {n1}.')
        elif n2 > n1:
            print(f'O maior número é {n2}.')
        else:
            print(f'Ambos os números são iguais a {n1}.')
    elif op == 4:
        print('\nVocê escolheu NOVOS NÚMEROS.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número:'))
    elif op == 5:
        print('\nVocê escolheu SAIR DO PROGRAMA.')
        print('Até mais.')
        break
    else: 
        print('Não entendi, por favor tente novamente.')
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))