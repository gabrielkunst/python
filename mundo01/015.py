"""  
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print('Bom dia, bem vindo ao aluguenow.net!')
km = float(input('Quantos Km foram rodados?'))
days = int(input('Por quantos dias você alugou o nosso veículo?'))
eq = (days*60) + (km*0.15)
print(f'Okay, você rodou {km}Km ao longo de {days} dias. O valor total de aluguel a ser pago é: R${eq:.2f}')