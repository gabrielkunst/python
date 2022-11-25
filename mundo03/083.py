"""  
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
open = []
close = []
eq = str(input('Digite uma expressão: '))
for i in eq:
    if i == '(':
        open.append(i)
    elif i == ')':
        close.append(i)
if len(open) == len(close):
    print('A expressão é válida!')
else: 
    print('A expressão é inválida!')
