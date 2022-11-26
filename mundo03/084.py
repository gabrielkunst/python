list = [[],[[],[]],[[],[]]] #lista 1 = nome, lista 2 = leve, lista 3 = pesados
while True:
    name = str(input('Digite o seu nome: ')).strip().lower()
    while True:
        weight = float(input('Digite o seu peso: '))
        if weight >= 100:
            list[0].append(name)
            list[2][0].append(name)
            list[2][1].append(weight)
            break
        elif 0 < weight < 100:
            list[0].append(name)
            list[1][0].append(name)
            list[1][1].append(weight)
            break
        else:
            print('Peso inválido, tente novamente.')
    while True:
        option = str(input('Deseja adicionar mais uma pessoa? S para sim ou N para não: ')).strip().upper()
        if option == 'N' or option == 'S':
            break
        else:
            print('Comando inválido, tente novamente.')
    if option == 'N':
        break
    else:
        continue
print(f'A lista formada foi: {list}')
print(f'Há nessa lista {len(list[0])} pessoas. ')
print(f'As pessoas mais pesadas são: {list[2][0]}, com respectivamente {list[2][1]}')
print(f'As pessoas mais leves são: {list[1][0]}, com respectivamente {list[1][1]}')
