"""  
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime
dic = {}
name = str(input('Nome: ')).strip().title()
birth = int(input('Ano de nascimento: '))
work_card = int(input('Código da carteira de trabalho: (0 = Não tenho) '))
dic['Nome'] = name
dic['Data de Nascimento'] = birth
dic['Idade'] = (datetime.today().year - birth)
dic['CTPS'] = work_card
if work_card == 0:
    for k, v in dic.items():
        print(f'{k} = {v}')
else:
    inicial_date = int(input('Ano de contratação: '))
    wage = int(input('Salário: R$'))
    dic['Ano de Contratação'] = inicial_date
    dic['Salário'] = wage
    apos = ((datetime.today().year - birth) + 35) - (datetime.today().year - inicial_date)
    dic['Aposentadoria'] = apos
    for k, v in dic.items():
        print(f'{k} = {v}')