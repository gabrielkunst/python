def escreva(msg):
    print('-'*(len(msg)))
    print(f'{msg}')
    print('-'*(len(msg)))
msg = str(input('Digite um frase:')).strip().title()
escreva(msg.center(len(msg)+4))