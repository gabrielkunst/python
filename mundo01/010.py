"""  
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
"""

name = str(input('Bom dia! Qual o seu nome?')).strip().title()
print(f'Seja bem vindo ao Cambio.net, {name}!')
v = float(input(f'Quantos reais você tem para trocar? R$'))
print(f'Ouww! Com R${v} você pode comprar ${v/(3.27):.2f}, meus parabéns!')
