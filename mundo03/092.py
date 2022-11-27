from datetime import date
dic = {}
name = str(input('Nome: ')).strip().title()
birth = int(input('Ano de nascimento: '))
work_card = int(input('Código da carteira de trabalho: (0 = Não tenho) '))
dic['Nome'] = name
dic['Data de Nascimento'] = birth
dic['Idade'] = (date.today().year - birth)
dic['CTPS'] = work_card
if work_card == 0:
    for k, v in dic.items():
        print(f'{k} = {v}')
else:
    inicial_date = int(input('Ano de contratação: '))
    wage = int(input('Salário: R$'))
    dic['Ano de Contratação'] = inicial_date
    dic['Salário'] = wage
    apos = ((date.today().year - birth) + 35) - (date.today().year - inicial_date)
    dic['Aposentadoria'] = apos
    for k, v in dic.items():
        print(f'{k} = {v}')