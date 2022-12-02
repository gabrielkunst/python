"""  
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

from time import sleep
numbers = [[], []]
for i in range(7):
    num = int(input('Digite um valor: '))
    if num%2 == 0:
        numbers[0].append(num)
        numbers[0].sort()
    else: 
        numbers[1].append(num)
        numbers[1].sort()
print(f'A lista formada foi {numbers}')
print(f'Os valores pares são: {numbers[0]}')
print(f'Os valores ímpares são: {numbers[1]}')

