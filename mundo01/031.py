"""  
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

print('Bom dia! Seja bem vindo ao pricecalculator.online!')
km = float(input('Quantos kilometros você percorreu?'))
if km < 200:
    print(f'O valor total da sua viagem é: R${km*(0.5):.2f}')
else: 
    print(f'O valor total da sua viagem é: R${km*(0.45):.2f}')