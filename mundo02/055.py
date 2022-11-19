"""  
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
max = 0
min = 0
for i in range(1,6):
    w = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        max = w
        min = w
    else: 
        if w > max:
            max = w
        if w < min:
            min = w
print(f'O maior peso é {max:.2f} e o menor peso é {min:.2f}.')
