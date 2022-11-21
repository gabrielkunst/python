"""  
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

n1 = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão da PA? '))
q = int(input('Quantos termos há nessa PA?'))
cont = 0
sum = 0
print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))
print(f'Os primeiros {q} termos dessa PA são::\n')

while cont != q:
    last = n1 + (q-1)*r
    sum = (q*(n1+last))/2
    cont += 1
    print(f'a{cont:<2} = {n1:<1} + {cont-1:<2} x {r:<2} = {n1+(cont-1)*r:<2}')

print(f'\nA soma dessa PA é {sum:.0f}')
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))


