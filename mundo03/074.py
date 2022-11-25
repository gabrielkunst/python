"""  
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint
nums = []
for i in range(5):
    nums.append(randint(0,1000))
nums = tuple(nums)
print(f'A tupla formada foi: {nums}')
print(f'O maior valor é {max(nums)}')
print(f'O menor valor é {min(nums)}')
