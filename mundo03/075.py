"""  
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""

num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
even_count = 0
list = []
print(f'Você digitou os valores: {num}.')
print(f'O menor valor é {min(num)}.')
print(f'O maior valor é {max(num)}.')
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes.')
else:
    print('O número 9 não foi digitado.')
if 3 in num:
    print(f'O primeiro número 3 apareceu na posição {num.index(3)}')
else:
    print('O número 3 não foi digitado.')
for i in range(0, len(num)):
    if num[i]%2 == 0:
        list.append(num[i])
        even_count += 1
if even_count > 0:
    print(f'Há na lista {even_count} números pares: {list}')
else:
    print('Não há números pares na lista.')
