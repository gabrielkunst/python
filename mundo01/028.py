""" 
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
num = random.randrange(6)
print('O sistema escolheu um valor.')
usernum = int(input('Qual foi o valor escolhido pelo sistema?'))
if usernum == num:
    print(f'Wowww, o valor escolhido foi {num} e você acertou, parabéns!')
else:
    print(f'O valor escolhido foi {num}, mas você escolheu {usernum}. Tente novamente!')
 