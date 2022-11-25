""" 
Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
name = str(input('Digite o seu nome: ')).strip().title()
print(f'Bom dia, {name}. Seja bem vindo(a)!')