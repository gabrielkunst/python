list = []
even = []
for i in range(4):
    num = int(input('Digite um valor inteiro: '))
    list.append(num)
list = tuple(list)
for i in range(4):
    if list[i]%2 == 0:
        even.append(list[i])
even = tuple(even)

print(f'Você digitou os valores {list}')
print(f'O valor 9 apareceu {list.count(9)} vezes.')
if 3 in list:
    print(f'O primeiro 3 foi digitado na posição {(list.index(3))+1}.')
else:
    print(f'O número 3 não foi digitado.')
if even != ():
    print(f'Os valores pares digitados foram {even}')
else: 
    print('Não digitado valor par algum.')
