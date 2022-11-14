import math
print('Seja bem vindo ao math.net, sua plataforma de calculos online!')
ca = float(input('Qual o valor do cateto adjacente?'))
co = float(input('Qual o valor do cateto oposto?'))
hip = math.hypot(ca, co)
print(f'O valor da hipotenusa desse triângulo é igual a: {hip:.2f}')