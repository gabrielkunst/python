quant = int(input('Quantos números você deseja adicionar? '))
list = []
for i in range(quant):
    num = int(input(f'Digite um valor para a posição {i+1}: '))
    if num in list:
        pass
    else: 
        list.append(num)
list.sort()
print(f'A lista formada foi: {list}')