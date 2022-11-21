"""  
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sex = ''
while sex != 1 or sex != 2:
    sex = int(input(''' Qual o seu gênero? 
    [1] Masculino
    [2] Feminino
    Escolha uma letra: '''))
    if sex == 1 or sex == 2:
        break
    else:
        print('Dado inválido! Tente novamente.')

if sex == 1:
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino.')
