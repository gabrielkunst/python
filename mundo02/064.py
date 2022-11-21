"""  
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
# variáveis 
value = ''
cont = 0
som = 0

# loop
while value != 999:
    cont += 1
    value = int(input('Digite um valor: '))
    som += value
print(f'Você digitou {cont-1} números. A soma destes é {som-999}.')