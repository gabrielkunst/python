"""  
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

from datetime import datetime
def voto(ano):
    if ano < 0:
        return print('Digite uma idade válida!')
    else:
        age = datetime.today().year - ano
        if 0 < age < 16:
            return print(f'Com {age} anos: NÃO VOTA')
        elif 16 <= age < 18 or age > 70:
            return print(f'Com {age} anos: VOTO OPCIONAL')
        elif 18 <= age < 70:
            return print(f'Com {age} anos: VOTO OBRIGATÓRIO')


ano = int(input('Data de nascimento: '))
voto(ano)