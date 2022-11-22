numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
option = ''

while True:
    num = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número escolhido foi {numbers[num].upper()}')
        while True:
            option = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
            if option == 'N' or option == 'S':
                break
            else:
                print('Digite um valor válido.')
        
    elif num > 20:
        print('Por favor, digite um número válido.')
    elif num < 0:
        print('Por favor, digite um número válido. ')
    if option == 'N':
        break
    