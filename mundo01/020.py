"""  
Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random
print('Bom dia, professor!')
st1 = str(input('Qual o nome do aluno 1?')).strip().title()
st2 = str(input('Qual o nome do aluno 2?')).strip().title()
st3 = str(input('Qual o nome do aluno 3?')).strip().title()
st4 = str(input('Qual o nome do aluno 4?')).strip().title()
lis = [st1, st2, st3, st4]
print(f'A lista formada foi: {lis}')
random.shuffle(lis)
print(f'A ordem formada para a apresentação do trabalho é: {lis}')