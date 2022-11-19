sex = ''
while sex != 1 or sex != 2:
    sex = int(input(''' Qual o seu gênero? 
    [1] Masculino
    [2] Feminino
    Escolha uma letra: '''))
    if sex == 1 or sex == 2:
        break

if sex == 1:
    print('Você é do sexo masculino.')
else:
    print('Você é do sexo feminino.')
