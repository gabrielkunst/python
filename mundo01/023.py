"""  
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

n = input('Escreva um número:')
x = [int(x) for x in str(n)]
print(f'{n} possui {len(n)} algarismos.')
print(f'{x}')
