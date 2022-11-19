print('Bom dia, seja bem vindo ao temper.net!')
num = float(input('Informe a temperatura:'))
print('''Qual métrica de temperatura você deseja? \n [1] Celsius para Fahrenheit \n [2] Fahrenheit para Celsius''')
option = int(input('Escolha um número:'))

cf = (num * (9/5) + 32)
fc = ((num - 32) * (5/9))

if option == 1:
    print(f'{num:.2f} celsius é igual a {cf:.2f} fahrenheit!')
elif option == 2:
    print(f'{num:.2f} fahrenheit é igual a {fc:.2f} celsius!')
else:
    print('Opção invalida. Tente novamente.')



