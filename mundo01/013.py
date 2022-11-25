"""  
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

v = float(input('Qual é o salário atual do funcionário?'))
dp = float(input('Quantos porcento de aumento?'))
dd = dp/(100)
print(f'O salário atualizado do funcionário será {v + (v*dd)}')