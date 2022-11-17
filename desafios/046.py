"""  
O programa deve fazer uma contagem regressiva de 10 até 0, com um segundo de intervalo.
1) Fazer um loop "for";
2) Adicionar um sleep, para fazer o intervalo de 1 segundo.
"""
from time import sleep
option = int(input('Digite 0 para iniciar o programa: '))
if option == 0:
    for x in range(10, 0, -1):
        print(f'\033[1;31m{x}\033[m')
        sleep(1)
    print('\033[1;32mFELIZ ANO NOVO!!!\033[m')
else: 
    print('Opção inválida! Tente novamente.')