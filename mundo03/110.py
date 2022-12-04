"""  
Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

import uteis
from time import sleep

#PROGRAMA PRINCIPAL
num = uteis.validadorfloat('Digite um número: ')
tu = uteis.validadorint('Porcentagem de aumento: ')
td = uteis.validadorint('Porcentagem de desconto: ')
uteis.resumo(num, tu, td)