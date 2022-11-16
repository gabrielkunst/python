"""  
1) O programa será um "simulador de empréstimo", deve ser perguntado o valor da casa, o salário da pessoa que deseja financiar e em quantos anos;
2) Calcular o valor da prestação mensal (não apresenta juros compostos);
3) A prestação mensal não pode exceder 30% do salário do indivíduo.
"""

from time import sleep

print('Seja bem vindo ao creditloan.net!')

name = input('Qual é o seu nome?')

price = float(input(f'Qual é o valor da casa que você deseja financiar, {name.title()}? R$'))

wage = float(input(f'{name.title()}, qual é o seu salário atual? R$'))

time = float(input(f'{name.title()}, em quantos anos você deseja quitar essa casa?'))

monthly = price/(time*12)

limit = (wage*30)/100

print('\033[1;32mAGUARDE...\033[m')

sleep(3)

if monthly > limit:
    print(f'{name.title()}, seu financiamento foi negado, porque as suas prestações excedem 30% do seu salário.')
else: 
    print(f'{name.title()}, seu financiamento foi aprovado, parabéns! Para continuar com o processo venha até nossa agência.')
    print('\033[1;36mResumo do seu financiamento:\033[m')
    print(f'Você pagará R${monthly:.2f} por mês durante 30 anos, totalizando R${price:.2f}.')
print('Obrigado por usar nossos serviços! Até mais.')

