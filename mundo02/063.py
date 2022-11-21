"""  
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8 
"""

#input
n = int(input('Quantos termos você deseja mostrar? '))

#variáveis/loop
t1 = 0
t2 = 1
cont = 3
print('A sequência é:',end=' ')
print(t1, t2, end=' ')
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1

