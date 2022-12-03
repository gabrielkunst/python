"""  
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
from time import sleep
def ajuda():
    while True:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format('MENU DE AJUDA'))
        print('\033[1;32m-\033[m'*40)
        comando = str(input('\033[1;32mComando: \033[m')).strip().lower()
        if comando == 'fim':
            print('\033[1;31mSAINDO...\033[m')
            print()
            sleep(2)
            break
        else:
            try:
                print(f'\033[1;34mACESSANDO O MANUAL DO COMANDO "{comando}"')
                print()
                sleep(2)
                help(comando)
            except ImportError:
                print('\033[1;31mERRO! Esse comando não existe\033[m')
ajuda()
    