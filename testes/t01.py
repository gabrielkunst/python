from time import sleep
itens = []
prices = []
count = 0
total = 0

print('{:-^40}' .format(' CADASTRE SEU PRODUTO '))
while True:
    name = str(input('\nDigite o nome do produto: ')).strip().lower()
    while True:
        price = float(input('Digite o preço do produto: R$'))
        if price > 0:
            break
        else: 
            print('O produto não pode ter valor igual a zero ou negativo!')
    print('\n{:-^40}' .format(' CADASTRANDO '))
    sleep(1)
    print('{:-^40}' .format(' PRODUTO CADASTRADO '))
    count += 1
    itens.append(name)
    prices.append(price)
    total += price
    while True: 
        opt = str(input('''\nDeseja cadastrar mais um produto? 
    [1] SIM
    [2] NÃO
    Digite um número: '''))
        if opt == '1' or opt == '2':
            break
        else: 
            print('Digite um valor válido! Tente novamente.')
    if opt == '2':
        print('Você escolheu SAIR.')
        break
sleep(1) 
print('\n{:-^40}' .format(' RESUMO DA COMPRA '))

if count == 1:
    print(f'Você comprou 1 produto.')
    print(f'O valor total foi R${total:.2f}')
else: 
    print(f'Você comprou {count} produtos.')
    print(f'O valor total foi de R${total:.2f}')
    lowest = prices.index(min(prices))
    higher = prices.index(max(prices))
    
    print(f'O produto mais barato custou R${min(prices):.2f} e esse produto foi: {itens[lowest]}')
    print(f'O produto mais caro custou R${max(prices):.2f} e esse produto foi: {itens[higher]}')
