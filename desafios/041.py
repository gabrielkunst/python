"""  
1) O programa deve receber a data de nascimento de uma pessoa e deve a classificar de acordo com a idade desta;
2)  Até 9 anos = mirim
    Até 14 anos = infantil
    Até 19 anos = junior
    Até 20 anos = sênior
    Acima de 20 anos = master
"""
from datetime import date
print('Seja bem vindo à CNN, Confederação Nacional de Natação!')
year = int(input('Em qual ano você nasceu?'))
current = date.today().year
age = (current - year)

if 0 <= age <= 9:
    print(f'Você tem {age} anos.')
    print('Você é classificado como um nadador mirim.')
elif 9 < age <= 14:
    print(f'Você tem {age} anos.')
    print('Você é classificado como um nadador infantil.')
elif 14 < age <= 19:
    print(f'Você tem {age} anos.')
    print('Você é considerado um nadador junior.')
elif 19 < age <= 25:
    print(f'Você tem {age} anos.')
    print('Você é considerado um nadador sênior.')
elif age > 25:
    print(f'Você tem {age} anos.')
    print('Você é considerado um nadador máster.')
else: 
    print('Tente novamente.') 