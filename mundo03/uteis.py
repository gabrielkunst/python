def aumentar(n=0, por=0):
    eq = (n*por)/100
    print(f'Aumentado o valor {n} em {por}%, temos {n+eq}')

def diminuir(n=0, por=0):
    eq = (n*por)/100
    print(f'Diminuindo o valor {n} em {por}%, temos {n-eq}')

def dobro(n=0):
    dob = n*2
    print(f'O dobro de {n} é {dob}')

def metade(n=0):
    met = n/2
    print(f'A metade de {n} é {met}')

def linha():
    print('\033[1;32m-\033[m'*40)

def aum(n=0,t=0,format=False):
    eq = n + (n*t)/100
    return eq if format is False else moeda(eq)

def dim(n=0,t=0,format=False):
    eq = n - (n*t)/100
    return eq if format is False else moeda(eq)

def met(n=0,format=False):
    eq = n/2
    return eq if format is False else moeda(eq)

def dob(n=0,format=False):
    eq = n*2
    return eq if format is False else moeda(eq)

def moeda(n=0,m='R$'):
    return f'{m}{n:.2f}'.replace('.',',')

def validador():
    while True:
        n = float(input('\033[1;32mDigite um valor: \033[m'))
        try:
            value = float(n)
            return value
        except ValueError:
            print('\033[1;31mERRO! Digite um valor VÁLIDO!\033[m') 

def resumo(n=0, tu=0, td=0):
    linha()
    print('{:^40}' .format('PAINEL'))
    linha()
#    print('{:<30}{:>10}' .format())
#fazer tabela
