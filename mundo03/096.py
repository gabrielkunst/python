"""  
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(a, b):
    print(f'A área do seu terreno {a} x {b} é igual a {a*b} metros quadrados.')
    print()
def anunciado():
    print('\033[1;32m-\033[m'*40)
    print('{:^40}' .format('RESULTADO'))
    print('\033[1;32m-\033[m'*40)


a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
anunciado()
area(a, b)