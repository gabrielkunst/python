rows = [[], [], []]
numbers = [[], []]
max2 = []
toteven = 0

for i in range(9):
    if i <= 2:
        num = int(input(f'Digite um valor para 1 x {i+1}: '))
        rows[0].append(num)
        if num%2 == 0:
            numbers[0].append(num)
            toteven += num
        else: 
            numbers[1].append(num)
    elif 2 < i <= 5:
        num = int(input(f'Digite um valor para 2 x {i+1}: '))
        rows[1].append(num)
        max2.append(num)
        if num%2 == 0:
            numbers[0].append(num)
            toteven += num
        else:
            numbers[1].append(num)
    elif 5 < i <= 8:
        num = int(input(f'Digite um valor para 3 x {i+1}: '))
        rows[2].append(num)
        if num%2 == 0:
            numbers[0].append(num)
            toteven += num
        else:
            numbers[1].append(num)
print(f'A matriz formada foi:')           
print(f'[{rows[0][0]:^5}] [{rows[0][1]:^5}] [{rows[0][2]:^5}]')
print(f'[{rows[1][0]:^5}] [{rows[1][1]:^5}] [{rows[1][2]:^5}]')
print(f'[{rows[2][0]:^5}] [{rows[2][1]:^5}] [{rows[2][2]:^5}]')
print('\n')
print(f'Os números pares digitados foram: {numbers[0]}')
print(f'Os números ímpares digitados foram: {numbers[1]}')
sum3 = rows[0][2] + rows[1][2] + rows[2][2]
print(f'A soma dos números pares é: {toteven}')
print(f'A soma dos valores da terceira coluna é: {sum3}')
print(f'O maior número da segunda linha é: {max(max2)}')