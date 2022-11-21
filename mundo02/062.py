"""  
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 
"""
# início da div
print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))

# inputs
n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
q = int(input('Digite a quantidade de termos da PA: '))
option = ''

# variáveis
som = 0
cont = 0

#loop
while cont != q:
    cont += 1
    last = (n1 + (q-1)*r)
    som = q*(last+n1)/2
    print(f'a{cont:<2} = {n1:<2} + {q-1:<2} x {r:<2} = {n1+(cont-1)*r:<2}')

option = int(input('''\nVocê deseja continuar?
[1] Sim
[2] Não
Escolha um número: '''))


#condição
if option == 1:
    add = int(input('\nQuantos termos você deseja adicionar? '))
    while cont != (q+add):
        cont += 1
        last = (n1 + ((q+add)-1)*r)
        som2 = (q+add)*(last+n1)/2
        print(f'a{cont:<2} = {n1:<2} + {(q+add)-1:<2} x {r:<2} = {n1+(cont-1)*r:<2}') 
    print(f'A soma da PA é {som2:.0f}')
elif option == 2:
    print('Ok, obrigado por usar nossos serviços.')
else:
    print('Você digitou um número inválido. Até mais.!')
    

# fim da div
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))