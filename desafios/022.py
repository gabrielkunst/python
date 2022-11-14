name = input('Bom dia, qual é o seu nome?')
split = name.strip()
first = name.split()
print('Veja o seu nome com algumas alterações:')
print(f'Tudo maiúsculo: {split.upper()}')
print(f'Tudo em minúsculo: {split.lower()}')
print(f'Possui {len(split.replace(" ", ""))} letras.')
print(f'O seu primeiro nome tem {len(first[0])} letras.')

