"""  
O programa deve ler o ano inputado pelo usuário e retornar se é ou não um ano bissexto.
1) input do ano
2) IF bissexto: print else: print

BISSEXTO:
- YEAR%4 = 0
- Caso termine com 00, YEAR/4 = 400
"""
from time import sleep
from datetime import date
print('Bom dia. Seja bem vindo ao bissexto.xyz!')
year = int(input('Qual é o ano que desejas verificar? Digite 0 caso queira verificar seu ano atual. \n'))
print('Espere enquanto calculo seu resultado...')
sleep(1)
print('Quase lá...')
sleep(2)
if year == 0:
    year = date.today().year
if (year%400) == 0 and (year%100) == 0:
    print(f'{year} é um ano BISSEXTO!')
elif (year%4) == 0 and (year%100) != 0:
    print(f'{year} é um ano BISSEXTO!')
else:
    print(f'{year} NÃO é um ano BISSEXTO!')

