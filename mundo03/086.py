rows = [[], [], []]

for i in range(9):
    if i <= 2:
        num = int(input(f'Digite um valor para 1 x {i+1}: '))
        rows[0].append(num)
    elif 2 < i <= 5:
        num = int(input(f'Digite um valor para 2 x {i+1}: '))
        rows[1].append(num)
    elif 5 < i <= 8:
        num = int(input(f'Digite um valor para 3 x {i+1}: '))
        rows[2].append(num)
print(f'{rows[0]}\n{rows[1]}\n{rows[2]}')