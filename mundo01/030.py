""" 
O programa deve ler um número e retornar se este é par ou ímpar.
1) Input do usuário
2) IF num%2 == 0: even num else: odd num
"""
from time import sleep
print('Bem vindo ao number-analysis.net!')
num = int(input('Qual o valor que desejas analisar?'))
eq = (num%2)
print('PROCESSANDO...')
sleep(2)
if eq == 0:
    print('O número analisado é PAR.')
else: 
    print('O número analisado é ÍMPAR.')
