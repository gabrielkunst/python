from time import sleep
list = [0,1,2,3,4,5,6,7,8,9,10]
listed = []
list_sort = []

def contador(a,b,c):
    print(f'Contagem de {a} até {b-1} de {c} em {c}')
    listed = list[a:b:c][:]
    if a < b:
        for c, i in enumerate(listed):
            print(f'{listed[c]}', end=' ', flush=True)
            sleep(0.5)
    else:
        list_sort = []
        list_sort = listed.sort(reverse=True)
        for c, i in enumerate(list_sort):
            print(f'{listed[c]}', end=' ', flush=True)
            sleep(0.5)
    print()


def linha():
    print()
    print('\033[1;32m-\033[m'*40)
    print()

linha()
contador(1,11,1)
linha()
contador(10,0,2)
linha()