"""  
1) O programa deve haver um input pedindo ao usuário qual base de conversão este deseja;
2) Uso de condições: 1 (binário), 2(octal) e 3(hexadecimal).
3) Pode usar bin, oct e hec.
"""

import inquirer
num = int(input('Digite um número inteiro:'))
list = ['Binário', 'Octal', 'Hexadecimal']
questions = [
    inquirer.List('types',
                message='Escolha uma opção de conversão:',
                choices=list,
                ),
]
answers = inquirer.prompt(questions)
selected = str(answers['types']).strip().lower()
bin_num = bin(num)[2:]
oct_num = oct(num)[2:]
hex_num = hex(num)[2:]


if selected == list[0].lower():
    print(f'O sistema escolhido foi {selected}!')
    print(f'O número {num} é igual a {bin_num} em binário.')
elif selected == list[1].lower():
    print(f'O sistema escolhido foi {selected}!')
    print(f'O número {num} é igual a {oct_num} em octal.')
elif selected == list[2].lower():
    print(f'O sistema escolhido foi {selected}!')
    print(f'O número {num} é igual a {hex_num} em hexadecimal.')
else:
    print('Tente novamente.')