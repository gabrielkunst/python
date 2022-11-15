""" 
O PROGRAMA DEVE LER A VELOCIDADE DE UM CARRO E RETORNAR SE ELE FOI MULTADO. (Vmax = 80km/h, Multa = R$7*km(acima do max))
1) QUAL FOI A VELOCIDADE DO CARRO
2) FOI MULTADO?
3) SE SIM, QUAL O VALOR DA MULTA
"""

print('Seja bem vindo ao multa.net.')
vel = float(input('Qual foi sua velocidade ao passar pelo radar?'))
if vel > 80:
    print(f'MULTADO! Você passou a {vel}km/h em um radar que é no máximo 80km/h')
    print(f'O valor da sua multa é: R${(vel-80)*7:.2f}')
else:
    print(f'Tudo certo, você não foi multado.')