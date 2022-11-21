"""  
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
# variáveis
soma = 0
cont = 0
option = ''
value = 0
list = []

# início da div
print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))

# loop
while option != 2:
    value = int(input('\nDigite um valor: '))
    soma += value
    cont += 1
    list.append(value)
    option = int(input('''\nDeseja continuar?
    [1] Sim
    [2] Não
    Escolha um número: '''))
    if option == 2:
        break
    elif option == 1:
        continue
    else: 
        print('\nDigite um número válido!\n')
    
print(f'\nVocê digitou {cont} números.')
print(f'O maior número é {max(list)}')
print(f'O menor número é {min(list)}')
print(f'A soma entre os números é {sum(list)}')

# fim da div
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))