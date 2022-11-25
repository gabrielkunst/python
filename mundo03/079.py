"""  
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

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