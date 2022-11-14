""" 
PROGRAMA QUE LÊ O NOME 01 E RETORNA SE O NOME 02 ESTÁ NA LISTA.
- Defini um padrão entre os nomes, ou seja, tudo minúsculo, depois foi feito a lista e baseado na lista + o nome dado, foi analisado se o nome escolhido estava nos colchetes.
"""

name = input('Digite o seu nome:')
namelow = name.lower()
isthere = input('Qual nome você deseja pesquisar se há na lista?')
istherelow = isthere.lower()
list = namelow.split()
print(f'A lista é: {list}')

try: 
    (list.index(istherelow))
    print(f'{istherelow.title()} se encontra na lista!')
except ValueError:
    print(f'{istherelow.title()} não está na lista.')

