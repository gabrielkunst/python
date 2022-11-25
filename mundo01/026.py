""" 
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

ph = str(input('Digite uma frase:')).strip()
phlow = ph.lower()
print(f"A sua frase possui: {phlow.count('a')} letras 'a'.")
print(f"A primeira letra 'a' aparece na posição {phlow.find('a')+1}.")
print(f"A última letra 'a' aparece na posição {phlow.rfind('a')+1 }")