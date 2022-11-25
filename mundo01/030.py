""" 
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
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
