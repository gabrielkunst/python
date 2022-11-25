"""  
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

list = []
for i in range(0,5):
    list.append(int(input(f'Digite o valor da posição {i+1}: ')))
print(f'A lista formada foi: {list}')
max_count = []
min_count = []
for i in range(len(list)):
    if list[i] == max(list):
        max_count.append(i)
for i in range(len(list)):
    if list[i] == min(list):
        min_count.append(i)

print(f'O maior número digitado foi: {max(list):2}, nas posições {max_count}')
print(f'O menor número digitado foi: {min(list):2}, nas posições {min_count}')


