"""  
O programa ler três comprimentos de reta e retornar se estas podem ou não formar um triângulo.
1) Input do comprimento das retas
2) Calcular se pode ou não formar um triângulo

EQ?
a + b > c
a + c > b
b + c > a

"""

print('Bom dia. Seja bem vindo ao matemática.net!')
a = float(input('Qual é o tamanho da primeira reta?'))
b = float(input('Qual é o tamanho da segunda reta?'))
c = float(input('Qual é o tamanho da terceira reta?'))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('SIM! É possível formar um triângulo com as retas fornecidas.')
else: 
    print('NÃO! Não é possível formar um triângulo com as retas fornecidas.')