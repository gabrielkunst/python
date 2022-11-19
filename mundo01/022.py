name = str(input('Bom dia, qual é o seu nome?')).strip()
first = name.split()
print('Veja o seu nome com algumas alterações:')
print(f'Tudo maiúsculo: {name.upper()}')
print(f'Tudo em minúsculo: {name.lower()}')
print(f'Possui {len(name.replace(" ", ""))} letras.')
print(f'O seu primeiro nome tem {len(first[0])} letras.')

