"""  
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

from math import trunc
v = float(input('Digite um número:'))
print(f'O número escolhido foi {v} e pode ser representado de forma inteira como: {trunc(v)}') 