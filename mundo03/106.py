def ajuda():
    while True:
        print('\033[1;32m-\033[m'*40)
        print('\033[1;32m{:^40}\033[m' .format('MENU DE AJUDA'))
        print('\033[1;32m-\033[m'*40)
        comando = str(input('\033[1;32mComando: \033[m')).strip().lower()
        if comando == 'fim':
            print('\033[1;31mSAINDO...\033[m')
            break
        else:
            try:
                print(f'\033[1;34mACESSANDO O MANUAL DO COMANDO "{comando}"')
                help(comando)
            except ImportError:
                print('\033[1;31mERRO! Esse comando não existe\033[m')
ajuda()
    