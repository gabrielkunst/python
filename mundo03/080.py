from time import sleep
list = []
count = 0
for i in range(3):
    num = int(input(f'Digite um valor para a posição {i}: '))
    list.append(num)
print(list)
for i in range(len(list)):
    print(list[i])
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]  
print(f'A lista formada foi: {list}')