""" PROGRAMA QUE LÊ O NOME DA CIDADE E RETORNA SE COMEÇA OU NÃO COM O NOME SANTOS.
"""

city = str(input('Digite o nome de uma cidade:')).strip()
sant = city.split()
default = sant[0].lower()
if default == 'santos':
    print('O nome da cidade começa com SANTOS!')
else:
    print('O nome da cidade não começa com SANTOS!') 