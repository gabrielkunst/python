""" 
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
"""

name = str(input('Digite um nome:')).strip
split = name.split()
print(f'Primeiro nome: {split[0].title()}')
print(f'Último nome: {split[-1].title()}')