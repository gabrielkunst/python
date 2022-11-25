"""  
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
"""

import math
degree = float(input('Qual o ângulo que você deseja calcular?'))
sen = math.sin(math.radians(degree))
cos = math.cos(math.radians(degree))
tg = math.tan(math.radians(degree))
print(f'O seno de {degree} é {sen:.2f}.')
print(f'O cosseno de {degree} é {cos:.2f}.')
print(f'A tangente de {degree} é {tg:.2f}.')
