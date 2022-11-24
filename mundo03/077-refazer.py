list = []
vowels = ('a', 'e', 'i', 'o', 'u')
while True:
    ph = str(input('\nDigite uma palavra: ')).strip().title()
    list.append(ph)
    while True:
        op = int(input('''\nVocê deseja adicionar mais uma palavra? 
    [1] SIM
    [2] NÃO
    Digite um valor: '''))
        if op == 1 or op == 2:
            break
        else:
            print('Digite um valor válido: ')
    if op == 2:
        break

list = tuple(list)
print(f'Você digitou a(s) palavra(s): {list}')
for i in range(0, len(list)):
    if i in vowels:
        print(f'Na palavra {list[i]} há {vowels} vogais.')