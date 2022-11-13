n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um outro valor:'))
op = input('Qual das operações a seguir você deseja fazer: soma, subtração, multiplicação ou divisão?')
if op == 'soma':
    print(f'A soma entre {n1} e {n2} é {n1+n2}')

if op == 'subtração':
    print(f'A subtração entre {n1} e {n2} é {n1-n2}')

if op == 'multiplicação':
    print(f'A multiplocação entre {n1} e {n2} é  {n1*n2}')

if op == 'divisão':
    print(f'A divisão entre {n1} e {n2} é {n1/n2}')
 