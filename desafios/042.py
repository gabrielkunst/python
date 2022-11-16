"""  
1) O programa deve ler 3 linhas de reta inseridas pelo usuário e retornar se estas linhas podem ou não formar um triângulo;
2) Uso de condições para retornar qual é o tipo de triângulo.
"""

from time import sleep
print('Bom dia, seja bem vindo ao math.net!')
a = float(input('Qual é o tamanho da primeira reta?'))
b = float(input('Qual é o tamanho da segunda reta?'))
c = float(input('Qual é o tamando da terceira reta?'))
print('\033[1;32mAGUARDE...\033[m')
sleep(3)
if a + b > c and a + c > b and b + c > a:
    print('SIM! É possível formar um triângulo.')
    if a == b == c:
        print('Trata-se de um triângulo equilátero, pois todos os lados são iguais.')
    elif a == b != c or a == c != b or b == c != a:
        print('Trata-se de um triângulo isósceles, pois dois lados são iguais.')
    else:
        print('Trata-se de um triângulo escaleno, pois todos os lados são diferentes.')
else: 
    print('NÃO! Não é possível formar um triângulo.')

