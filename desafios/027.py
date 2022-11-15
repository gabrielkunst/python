""" 
O PROGRAMA DEVE LER O NOME DA PESSOA E DEFINIR O PRIMERO E O ÚLTIMO NOME, E MOSTRÁ-LOS SEPARADAMENTE.
"""

name = str(input('Digite um nome:')).strip
split = name.split()
print(f'Primeiro nome: {split[0].title()}')
print(f'Último nome: {split[-1].title()}')