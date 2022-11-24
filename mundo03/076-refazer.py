from time import sleep
list = []
count = -1

while True:
    name = str(input('\nDigite o nome do produto: ')).strip().lower()
    price = float(input('Digite o preço do produto: R$'))
    print('{:-^40}' .format(' CADASTRANDO '))
    sleep(1)
    print('{:-^40}' .format(' PRODUTO CADASTRADO '))
    count += 1
    list.append(name)
    list.append(price)
    opt = int(input('''\nDeseja cadastrar mais um produto? 
    [1] SIM
    [2] NÃO
    Digite um número: '''))
    while True: 
        if opt == 1 or opt == 2:
            break
        else: 
            print('Digite um valor válido! Tente novamente.')
    if opt == 2:
        print('Você escolheu SAIR.')
        break

print(list[0:len(list):2])    