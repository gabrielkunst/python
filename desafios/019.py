import random
print('Bom dia, professor!')
st1 = input('Qual o nome do primeiro aluno?')
st2 = input('Qual o nome o segundo aluno?')
st3 = input('Qual o nome do terceiro aluno?')
st4 = input('Qual o nome do quarto aluno?')
lis = [st1, st2, st3, st4]
print(f'A lista formada foi {lis}. Aguarde enquanto escolho o aluno(a)...')
print(f'O aluno escolhido foi: {random.choice(lis)}!')
