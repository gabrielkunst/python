"""  
1) O programa deve ler dois números e retornar qual é o maior e qual é o menor, ou até se ambos são iguais.
"""

from time import sleep
num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite mais um número inteiro:'))
print('\033[1;32mAGUARDE...\033[m')
sleep(3)
if num1 > num2:
    print(f'O maior número é {num1}!')
    print(f'O menor número é {num2}!')
elif num1 < num2:
    print(f'O maior número é {num2}!')
    print(f'O menor número é {num1}!')
else:
    print(f'Os números são iguais, logo não há maior ou menor.')