"""  
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

city = str(input('Digite o nome de uma cidade:')).strip()
sant = city.split()
default = sant[0].lower()
if default == 'santos':
    print('O nome da cidade começa com SANTOS!')
else:
    print('O nome da cidade não começa com SANTOS!') 