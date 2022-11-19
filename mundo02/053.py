"""  
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

name = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
print(f'O contrário de {name.title()} é igual a {name[::-1].title()}')
if name == name[::-1]:
    print('SIM, essa sentença é um palíndromo.')
else:
    print('NÃO, essa sentença não é um palíndromo.')