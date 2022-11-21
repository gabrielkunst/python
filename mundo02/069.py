import inquirer
count = 0
list = []
gender = ''
option = ''
man = 0
age_count = 0
womanlesstwenty = 0


print('\033[1;32m{:-^40}\033[m' .format(' INÍCIO '))

while True:
    print(f'\nPESSOA {count+1}:')
    name = str(input('\nDigite o seu nome: ')).strip().lower()
    age = int(input('Digite a sua idade: '))
    gender = str(input('Digite o seu gênero: [M/F] ')).strip().lower()
    while gender != 'm' and gender != 'f':
        gender = str(input('Digite o seu gênero: [M/F] ')).strip().lower() 
    option = str(input('Deseja continuar? [S/N] ')).strip().lower()
    while option != 's' and option != 'n':
            option = str(input('Deseja continuar? [S/N] ')).strip().lower()
    count += 1
    list.extend([name, age, gender])
    if age > 18:
        age_count += 1
    if gender == 'm':
        man += 1
    if gender == 'f' and age < 20:
        womanlesstwenty += 1
    if option == 'n':
        break
print(f'\nAo todo há {count} pessoas.')
print(f'Há {age_count} pessoas com mais de 18 anos.')
print(f'Há {man} homens cadastrados.')
print(f'Há {womanlesstwenty} mulheres com menos de 20 anos.')
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))
