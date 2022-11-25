"""  
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

list = []
evenlist = []
oddlist = []
count = 0

quant = int(input('Quantos valores você deseja digitar? '))
for i in range(quant):
    num = int(input(f'Digite um valor para a posição {i}: '))
    if num%2 == 0:
        list.append(num)
        evenlist.append(num)
        count += 1
    else:
        list.append(num)
        oddlist.append(num)
        count += 1
print(f'Você digitou {count} números')
print(f'A lista formada foi: {list}')
print(f'Os números pares digitados foram: {evenlist}')
print(f'Os números ímpares digitados foram: {oddlist}')