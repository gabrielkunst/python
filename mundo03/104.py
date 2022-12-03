"""  
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('ERRO! Digite um número inteiro!')
        else:
            return n

#Programa Principal
n = leiaint('Digite um valor:')
print(f'Você digitou o valor: {n}.')