"""  
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

words = ('monitor', 'mouse', 'teclado', 'mousepad', 'pedro', 'mario', 'cooler', 'ram', 'fonte', 'caixa', 'prego')
for i in words:
    print(f'\nA palavra {i} apresenta: ', end='')
    for letter in i:
        if letter in 'aeiou':
            print(letter, end=' ')