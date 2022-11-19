"""  
1) O programa deve ler a data de nascimento de um jovem e retornar se ele irá se alistar, se está na hora de se alistar ou se já passou da hora de se alistar.
2) Deve, também, mostrar o prazo até se alistar, ou se for o caso, o tempo que já passou do alistamento.
"""

from datetime import date
year = int(input('Qual ano você nasceu?'))
current = date.today().year
eq = (current - year)

if eq == 18:
    print(f'Você tem {eq} anos.')
    print('Jovem, está na hora de você se alistar nas forças armadas.')
elif eq < 18:
    print(f'Você tem {eq} anos.')
    print(f'Jovem, faltam {(18-eq)} anos para o seu alistamento.')
elif eq > 18:
    print(f'Você tem {eq} anos.')
    print(f'Jovem, o seu ano de alistamento foi há {(eq-18)} anos atrás. Caso não tenha se apresentado, direcione-se ao quartel mais próximo.')