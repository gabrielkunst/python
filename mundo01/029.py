""" 
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

print('Seja bem vindo ao multa.net.')
vel = float(input('Qual foi sua velocidade ao passar pelo radar?'))
if vel > 80:
    print(f'MULTADO! Você passou a {vel}km/h em um radar que é no máximo 80km/h')
    print(f'O valor da sua multa é: R${(vel-80)*7:.2f}')
else:
    print(f'Tudo certo, você não foi multado.')