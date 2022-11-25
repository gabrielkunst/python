"""  
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número:'))
n3 = int(input('Insira o terceiro número:'))

if n1 > n2 > n3 or n1 > n3 > n2:
    biggest = n1
if n2 > n1 > n3 or n2 > n3 > n1:
    biggest = n2
if n3 > n1 > n2 or n3 > n2 > n1:
    biggest = n3

if n1 < n2 < n3 or n1 < n3 < n2:
    smallest = n1
if n2 < n1 < n3 or n2 < n3 < n1:
    smallest = n2
if n3 < n2 < n1 or n3 < n1 < n2:
    smallest = n3

print(f'O menor número é {smallest}.')
print(f'O maior número é {biggest}.')