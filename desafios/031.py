"""  
O programa deve ler o input do usuário e definir se a passagem é 0,5/km ou 0,45/km e retornar o preço que este deve pagar.
1) Qual a distância
2) Condição
"""

print('Bom dia! Seja bem vindo ao pricecalculator.online!')
km = float(input('Quantos kilometros você percorreu?'))
if km < 200:
    print(f'O valor total da sua viagem é: R${km*(0.5)}')
else: 
    print(f'O valor total da sua viagem é: R${km*(0.45)}')