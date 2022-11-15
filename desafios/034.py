"""  
O programa deve ler o salário de um funcionário e retornar se ele terá 10 ou 15% de aumento, baseado em 1250 reais (maior que isso é 10%, menor é 15%.)
"""

name = input('Bom dia. Qual é o nome do funcionário?')
wage = float(input(f'Qual é o salário do {name.title()}?'))
ten = ((wage*10)/100) + wage
fif = ((wage*15)/100) + wage
if wage <= 1250:
    print(f'O {name.title()} terá 15% de aumento, seu novo salário é: R${fif}.')
else:
    print(f'O {name.title()} terá 10% de aumento, seu novo aumento será R${ten}. ')
