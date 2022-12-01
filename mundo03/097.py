"""  
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                            
"""

def escreva(msg):
    print('-'*(len(msg)))
    print(f'{msg}')
    print('-'*(len(msg)))
msg = str(input('Digite um frase:')).strip().title()
escreva(msg.center(len(msg)+4))