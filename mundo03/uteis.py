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

def validadorfloat(msg):
    while True:
        try:
            value = float(input(msg))
        except ValueError:
            print('\033[1;31mERRO! Digite um valor VÁLIDO!\033[m') 
            continue
        else:
            return value
        

def resumo(n=0, tu=0, td=0):
    linha()
    print('{:^40}' .format('PAINEL'))
    linha()
    print(f'Preço analisado: \t\t{moeda(n)}')
    print(f'Aumentando em {tu}%: \t\t{moeda(aum(n, tu))}')
    print(f'Diminuindo em {td}%: \t\t{moeda(dim(n, td))}')
    print(f'Metade do preço: \t\t{moeda(met(n))}')
    print(f'Dobro do preço: \t\t{moeda(dob(n))}')
    linha()

def validadorint(msg):
    while True:
        try:
            value = int(input(msg))
        except ValueError:
            return '\033[1;31mERRO! Digite um valor VÁLIDO!\033[m'
        else:
            return value


