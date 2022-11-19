"""  
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão desta PA: '))
print('\033[1;32m{:=^40}\033[m' .format(' RESULTADO DA PA '))  
for x in range(10):
    print(f'{num} + {raz} x {x} = {num+(raz*x)}')
print('\033[1;32m{:=^40}\033[m' .format(' FIM '))  