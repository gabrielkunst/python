import random
from time import sleep
print('Bom dia, professor!')
st1 = str(input('Qual o nome do primeiro aluno?')).strip().title()
st2 = str(input('Qual o nome o segundo aluno?')).strip().title()
st3 = str(input('Qual o nome do terceiro aluno?')).strip().title()
st4 = str(input('Qual o nome do quarto aluno?')).strip().title()
lis = [st1, st2, st3, st4]
print(f'A lista formada foi {lis}. Aguarde enquanto escolho o aluno(a)...')
sleep(3)
print(f'O aluno escolhido foi: {random.choice(lis)}!')
