"""  
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

name = str(input('Bom dia, qual é o seu nome?')).strip()
first = name.split()
print('Veja o seu nome com algumas alterações:')
print(f'Tudo maiúsculo: {name.upper()}')
print(f'Tudo em minúsculo: {name.lower()}')
print(f'Possui {len(name.replace(" ", ""))} letras.')
print(f'O seu primeiro nome tem {len(first[0])} letras.')

