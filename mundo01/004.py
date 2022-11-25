"""  
Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

v = input('Digite algo:')
print(f'A classe primitiva de {v} é: {type(v)}')
print(f'É tudo maiúsculo? {v.isupper()}')
print(f'É tudo minúsculo? {v.islower()}')
print(f'É alfabético? {v.isalpha()}')
print(f'É alfanumérico? {v.isalnum()}')
print(f'Só tem espaços? {v.isspace()}')
