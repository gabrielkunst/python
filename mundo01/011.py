"""  
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

name = str(input('Bom dia! Qual o seu nome?')).strip().title()
print(f'Seja bem vindo ao Panorama Center, a melhor loja de construção para sua casa, {name}!')
w = float(input('Quantos metros de largura há sua parede?'))
h = float(input('Quantos metros de altura há sua parede?'))
a = w*h
print(f'Okay, sua parede tem {a} metros quadrados.')
print(f'Para pintar sua parede serão necessários {a/2} litros de tinta.')

