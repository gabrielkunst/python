"""  
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

rows = [[], [], []]

for i in range(9):
    if i <= 2:
        num = int(input(f'Digite um valor para 1 x {i+1}: '))
        rows[0].append(num)
    elif 2 < i <= 5:
        num = int(input(f'Digite um valor para 2 x {i+1}: '))
        rows[1].append(num)
    elif 5 < i <= 8:
        num = int(input(f'Digite um valor para 3 x {i+1}: '))
        rows[2].append(num)
print(f'[{rows[0][0]:^5}] [{rows[0][1]:^5}] [{rows[0][2]:^5}]')
print(f'[{rows[1][0]:^5}] [{rows[1][1]:^5}] [{rows[1][2]:^5}]')
print(f'[{rows[2][0]:^5}] [{rows[2][1]:^5}] [{rows[2][2]:^5}]')