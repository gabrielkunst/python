from datetime import date


print('''Você é homem ou mulher? \n [1] Homem \n [2] Mulher''')
sex = int(input('Escolha um número:'))
if sex == 1:
    print('Você é homem, logo o alistamento é obrigatório.')
    year = int(input('Em qual ano você nasceu, jovem?'))
    current = date.today().year
    age = (current - year)
    if age == 18:
        print(f'Você tem {age} anos.')
        print(f'Você DEVE se alistar neste ano, jovem!')
    elif age < 18:
        print(f'Você tem {age} anos.')
        print(f'Faltam {18-age} anos para o seu alistamento, jovem!')
        print(f'O seu alistamento será em: {year+18}!')
    elif age > 18:
        print(f'Você tem {age} anos.')
        print(f'O seu alistamento já passou. Foi há {age-18} anos atrás.')
        print(f'O seu alistamento foi em: {current-(age-18)}!')

elif sex == 2:
    print('Você é mulher, logo não precisa se alistar.')

else:
    print('Opção inválida. Tente novamente.')