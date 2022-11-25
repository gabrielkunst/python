"""  
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

name = input('Bom dia. Qual é o nome do funcionário?')
wage = float(input(f'Qual é o salário do {name.title()}?'))
ten = ((wage*10)/100) + wage
fif = ((wage*15)/100) + wage
if wage <= 1250:
    print(f'O {name.title()} terá 15% de aumento, seu novo salário é: R${fif:.2f}.')
else:
    print(f'O {name.title()} terá 10% de aumento, seu novo aumento será R${ten:.2f}. ')
