"""  
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(n, show=False):
    """
    --> Fatorial de um número
    :param n --> Número a ser calculado
    :param show --> Determina se será mostrado o calculo.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            count = i
            if count != 1: 
                print(f'{i} x ', end='')
            else: print(f'{i} = ', end='')

    return print(f)

n = int(input('Valor: '))
fatorial(n, show=True)
