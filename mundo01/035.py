"""  
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
from time import sleep
print('Bom dia. Seja bem vindo ao matemática.net!')
a = float(input('Qual é o tamanho da primeira reta?'))
b = float(input('Qual é o tamanho da segunda reta?'))
c = float(input('Qual é o tamanho da terceira reta?'))
print('TENTANDO FORMAR O TRIÂNGULO...')
sleep(3)
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('SIM! É possível formar um triângulo com as retas fornecidas.')
else: 
    print('NÃO! Não é possível formar um triângulo com as retas fornecidas.')