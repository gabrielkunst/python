"""  
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário.
"""

def notas(*num, sit=False):
    """
    --> Retorna um conjunto de dados sobre certas notas.
    :param num --> Notas a serem calculadas
    :param sit -->
    """
    dic = {}
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    dic['média'] = sum(num)/len(num)
    dic['total'] = len(num)
    if sit:
        if dic['média'] >= 8:
            dic['sit'] = 'BOM'
        elif dic['média'] >= 6:
            dic['sit'] = 'RAZOÁVEL'
        else:
            dic['sit'] = 'RUIM'
    return dic

resp = notas(9,10,9,7,10, sit=True)
print(resp)
