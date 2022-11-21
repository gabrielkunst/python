"""  
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import choice
pc = choice(range(0,101))
user = ''
attempt = 0
while user != pc:
    user = int(input('Adivinhe o meu número: '))
    attempt += 1
    if user > pc:
        print('Menos... Tente novamente.')
    else: 
        print('Mais... Tente novamente.')
print(f'\033[1;32mVocê acertou!\033[m O sistema escolheu {pc}.')
print(f'Foi necessário \033[1;32m{attempt}\033[m tentativas para você acertar!')