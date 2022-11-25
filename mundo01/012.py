""" 
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

v = float(input('Qual é o valor do produto?'))
dp = float(input('Quantos porcento de desconto será aplicado?'))
dd = dp/(100)
print(f'O valor final do produto será: {v-(v*dd):.2f}')