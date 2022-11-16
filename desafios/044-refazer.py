"""  
1) O programa deve receber a opção de pagamento e retornar a quantidade de desconto sobre um produto;
2)  Dinheiro/Cheque = 10%
    Cartão = 5%
    2x no cartão = preço normal
    3x ou mais no cartão = 20% de juros (no total, não por mês)
"""

from time import sleep
print('Olá, tudo bem?')
price = float(input('Qual é o valor total do produto? R$'))

sleep(1)
list = ['Dinheiro', 'Cheque', '1x Cartão', '2x Cartão', '3x Cartão', '+3x Cartão']
print(list)

sleep(1)
meth = str(input('Qual dos meios de pagamento disponíveis você deseja?')).strip()

ten = price - (price*10)/100
fiv = price - (price*5)/100
twen = price + (price*20)/100









#testes

""" 
if meth.lower() == list[0].lower() or list[1].lower():
    print(f'O valor total do produto será R${ten:.2f}.')
elif meth.lower() == list[2].lower():
    print(f'O valor total do produto será R${fiv:.2f}.')
elif meth.lower() == list[3].lower():
    print(f'O valor total do produto será R${price:.2f}.')
elif meth.lower() == list[4].lower() or list[5].lower():
    print(f'O valor total do produto será R${twen:.2f}.')
else:
    print('Tente novamente.')

 """