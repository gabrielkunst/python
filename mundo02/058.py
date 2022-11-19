from random import choice
pc = choice(range(0,11))
user = ''
attempt = 0
while user != pc:
    user = int(input('Adivinhe o meu número: '))
    attempt += 1
print(f'\033[1;32mVocê acertou!\033[m O sistema escolheu {pc}.')
print(f'Foi necessário \033[1;32m{attempt}\033[m tentativas para você acertar!')