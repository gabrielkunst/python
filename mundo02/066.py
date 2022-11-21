value = 0
count = 0
sum = 0
mult = 0

print('\033[1;32m{:-^40}\033[m'  .format(' INÍCIO '))
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    count += 1
    sum += n
print(f'Você digitou {count} números, a soma destes é {sum}.')
print('\033[1;32m{:-^40}\033[m' .format(' FIM '))