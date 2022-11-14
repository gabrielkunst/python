""" 
O PROGRAMA DEVE LER O NOME DA PESSOA E DEFINIR O PRIMERO E O ÚLTIMO NOME, E MOSTRÁ-LOS SEPARADAMENTE.
- Primeiro dividi o nome formando uma lista e depois se escolhe o primeiro e o último item da lista.
"""

name = input('Digite um nome:')
split = name.split()
print(f'Primeiro nome: {split[0].title()}')
print(f'Último nome: {split[-1].title()}')