def leiaint(msg):
    while True:
        try: 
            n = int(input(msg))
        except ValueError:
            print('ERRO! Digite um número inteiro válido!')
        else:
            return n

#PROGRAMA PRINCIPAL
n = leiaint('Valor: ')
print(f'Você digitou o número {n}')
