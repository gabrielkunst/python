from time import sleep
import inquirer
num = int(input('Digite um número inteiro:'))
sleep(1)


""" list = ['Binário', 'Octal', 'Hexadecimal']
questions = [
    inquirer.List('options',
    message='Escolha o sistema de conversão:',
    choices=list
    ),
]

bin = bin(num)[2:]
oct = oct(num)[2:]
hex = hex(num)[2:]


answers = inquirer.prompt(questions)
cho = (answers['options']).lower()

print('\033[1;32mAGUARDE...\033[m')
sleep(3)

if cho == list[0].lower():
    print(bin)

elif cho == list[1].lower():
    print(oct)

elif cho == list[2].lower():
    print(hex)

else:
    print('Tente novamente!')


 """


print('''Escolha o sitema de conversão:\n [1] Binário \n [2] Octal \n [3] Hexadecimal''')

selected = int(input('Sua opção:'))
bin = bin(num)[2:]
oct = oct(num)[2:]
hex = hex(num)[2:]

if selected == 1:
    print(bin)
elif selected == 2:
    print(oct)
elif selected == 3:
    print(hex)
else:
    print('Opção inválida! Tente novamente.')

