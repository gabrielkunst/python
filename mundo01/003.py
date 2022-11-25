"""  
Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.
"""

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um outro valor:'))
op = str(input('Qual das operações a seguir você deseja fazer: soma, subtração, multiplicação ou divisão?')).strip().lower()
if op == 'soma':
    print(f'A soma entre {n1} e {n2} é {n1+n2}')
elif op == 'subtração':
    print(f'A subtração entre {n1} e {n2} é {n1-n2}')
elif op == 'multiplicação':
    print(f'A multiplocação entre {n1} e {n2} é  {n1*n2}')
elif op == 'divisão':
    print(f'A divisão entre {n1} e {n2} é {n1/n2}')
else:
    print('Escolha uma alternativa valida.')
 