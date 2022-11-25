"""  
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

from time import sleep
list = []
count = 0
for i in range(5):
    num = int(input(f'Digite um valor para a posição {i}: '))
    list.append(num)
print(list)
for i in range(len(list)):
    print(list[i])
    for pos in range(i+1, len(list)):
        if list[i] > list[pos]:
                list[i], list[pos] = list[pos], list[i]  
print(f'A lista formada foi: {list}')

