import random
print('Bom dia, professor!')
st1 = input('Qual o nome do aluno 1?')
st2 = input('Qual o nome do aluno 2?')
st3 = input('Qual o nome do aluno 3?')
st4 = input('Qual o nome do aluno 4?')
lis = [st1, st2, st3, st4]
print(f'A lista formada foi: {lis}')
random.shuffle(lis)
print(f'A ordem formada para a apresentação do trabalho é: {lis}')