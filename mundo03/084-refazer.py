list = []



while True:
    name = str(input('Nome: ')).strip().title()
    weight = float(input('Peso: '))
    info = [name, weight]
    list.append(info[:])
    while True:
        option = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if option in 'Ss':
            break
        elif option in 'Nn':
            break
        else:
            print('Comando inválido, tente novamente.')
    if option in 'Nn':
        break
print(f'Há no total {len(list)} pessoas.')


