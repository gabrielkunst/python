price_count = 0
option = ''
count = 0
total = 0
high = 0
low = 0
list = []

print('{:-^40}' .format(' INÍCIO '))
while True:
    count += 1
    name = str(input('\nQual é o nome do produto? ')).strip().lower()
    price = float(input('Qual o valor pago no produto? R$'))
    total += price
    if price > 1000:
        price_count += 1
    option = str(input('Você deseja continuar? [S/N] ')).strip().lower()
    while option != 's' and option != 'n':
        option = str(input('Você deseja continuar? [S/N] ')).strip().lower()
    if option == 'n':
        break
print('\n{:-^40}' .format(' RESUMO '))
print(f'Você comprou {count} itens.')
print(f'Você comprou {price_count} itens acima de R$1000 reais.')
print(f'Você gastou no total R${total:.2f}. ')
print('{:-^40}' .format(' FIM '))