"""  
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

list = ('Teclado', 100, 'Mouse', 90, 'Mousepad', 50, 'Monitor', 300)
total = 0
print('{:-^50} ' .format(' CUPOM FISCAL '))

for i in range(0, len(list)):
    if i%2 == 0:
        print('{:.<40} ' .format(list[i]), end='')
    else:
        print(f'R${list[i]:.2f}')
        total += list[i]
print('{:.<40} ' .format('TOTAL'), end='')
print(f'R${total:.2f}')
print('{:-^50}' .format(' FIM '))