"""  
O programa deve ler 3 números inserido pelo usuário e dizer qual é o menor e qual é o maior.
"""

n1 = float(input('Insira o primeiro número:'))
n2 = float(input('Insira o segundo número:'))
n3 = float(input('Insira o terceiro número:'))

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