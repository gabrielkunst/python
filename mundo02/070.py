"""  
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. 
"""
count = 0
itens = []
prices = []
total = 0
hundred_count = 0

print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))
while True:
    name = str(input('\nDigite o nome do produto: ')).strip().lower()
    price = float(input('Digite o valor do produto: R$'))
    count += 1
    itens.append(name)
    prices.append(price)
    total += price
    if price > 1000:
        hundred_count += 1
    while True:
        option = int(input('''Você deseja continuar? 
        [1] SIM, ADICIONAR UM NOVO PRODUTO
        [2] NÃO, SAIR DO PROGRAMA
        Digite um número: [1/2] '''))
        if option == 1 or option == 2:
            break
        else:
            print('Digite um valor válido, tente novamente.')
    if option == 2:
        break
print('\n\033[1;32m{:-^40}\033[m' .format(' RESUMO DA COMPRA '))
print(f'Você comprou ao todo {count} itens.')
print(f'Você gastou no total R${total:.2f}')
print(f'Você comprou {hundred_count} itens que custam mais de R$1000')
print(f'O produto mais barato que você comprou foi {itens[prices.index(min(prices))]}, custando R${min(prices):.2f}')
print('\n\033[1;32m{:-^40}\033[m' .format(' FIM '))


