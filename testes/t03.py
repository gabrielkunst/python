total = 0

print('{:-^40}' .format(' BANCO GKZ '))
name = str(input('Digite o seu nome: ')).strip().lower()
account = int(input('Digite o número da conta: '))

while True:
    option = int(input('''\nO que deseja fazer?
[1] Depósito
[2] Retirada
[3] Extrato
[4] Sair
Digite um número: '''))
    if option == 1:
        while True:
            deposit = float(input('Qual é o valor do depósito? R$'))
            if deposit > 0:
                print(f'Você depositou R${deposit:.2f}')
                total += deposit
                print(f'O seu saldo é de R${total:.2f}')
                break
            else:
                print(
                    f'Não há como depositar R${deposit:.2f}. Tente novamente.')
    if option == 2:
        while True:
            if total > 0:
                withdrawl = float(input('Qual é o valor da retirada? R$'))
                if withdrawl > total:
                    print('Você não tem esse valor para retirada.')
                    print(f'Você tem um saldo de R${total:.2f}')
                elif withdrawl <= 0:
                    print(
                        f'Não há como retirar R${withdrawl:.2f}. Tente novamente.')
                else:
                    print(f'Você retirou R${withdrawl:.2f}')
                    total -= withdrawl
                    print(f'Você ainda tem um saldo de R${total:.2f}')
                    break
    if option == 3:
        print('\n')
        print('{:-^40}' .format(' EXTRATO '))
        print(f'Nome: {name.title()}')
        print(f'Conta: {account}')
        if total > 0:
            print(f'Saldo >> {total:.2f}')
        else:
            print('{:->40}' .format(' R$0'))
        print('{:-^40}' .format(' VOLTE SEMPRE '))
