""" 
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

name = str(input('Digite o seu nome:')).strip()
namelow = name.lower()
isthere = str(input('Qual nome você deseja pesquisar se há na lista?')).strip()
istherelow = isthere.lower()
list = namelow.split()
print(f'A lista é: {list}')

try: 
    (list.index(istherelow))
    print(f'{istherelow.title()} se encontra na lista!')
except ValueError:
    print(f'{istherelow.title()} não está na lista.')

