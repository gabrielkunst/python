"""  
1) O programa deve receber a opção de pagamento e retornar a quantidade de desconto sobre um produto;
2)  Dinheiro/Cheque = 10%
    Cartão = 5%
    2x no cartão = preço normal
    3x ou mais no cartão = 20% de juros (no total, não por mês)
"""

import inquirer
from time import sleep
price = float(input('Qual é o valor total do produto? R$'))
list = ['Dinheiro', 'Cheque', '1x Cartão', '2x Cartão', '3x ou +3x Cartão']
questions = [
    inquirer.List('language',
                message = 'Escolha a forma de pagamento:',
                choices = list,
                ),
]
answers = inquirer.prompt(questions)

ten = price - (price*10)/100
fiv = price - (price*5)/100
twe = price + (price*20)/100

print('\033[1;31mAGUARDE...\033[m')
sleep(2)

option = str(answers['language']).lower()
if option == list[0].lower():
    print(f'O valor do produto será R${ten:.2f}.')
elif option == list[1].lower():
    print(f'O valor do produto será R${ten:.2f}.')
elif option == list[2].lower():
    print(f'O valor do produto será R${fiv:.2f}.')
elif option == list[3].lower():
    print(f'O valor do produto será R${price:.2f}.')
elif option == list[4].lower():
    print(f'O valor do produto será R${twe:.2f}.')
else:
    print('Tente novamente.')

print('\033[1;32mObrigado por usar os nossos serviços!\033[m')