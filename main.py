option = 1
while option == 1:
    num = int(input('Digite um valor inteiro: '))
    for i in range(1,11):
        print(f'{i:2} x {num:2} = {num*i:2}')
    option = int(input('''Você deseja multiplicar mais um número?
[1] Sim
[2] Não
Sua escolha: '''))
print('FIM')
