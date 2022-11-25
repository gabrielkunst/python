list = []
count = 0
count5 = 0
quant = int(input('Quantos números você deseja digitar? '))
for i in range(quant):
    num = int(input(f'Digite um número para a posição {i}: '))
    list.append(num)
    count += 1
    if num == 5:
        count5 += 1
print(f'Você digitou {count} números')
print(f'A lista formada em ordem decrescente é {sorted(list, reverse=True)}')
if 5 in list:
    print(f'O 5 foi digitado e apareceu {list.index(5)} vezes.')
else:
    print('O número 5 não foi digitado.')