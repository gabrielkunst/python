""" PROGRAMA QUE LÊ O NOME DA CIDADE E RETORNA SE COMEÇA OU NÃO COM O NOME SANTOS.
- Defini um padrão entre o nome da cidade e santos, ou seja, tudo minúsculo, depois foi feita a condição se o nome da cidade começa ou não com SANTOS.
"""

city = input('Digite o nome de uma cidade:')
sant = city.split()
default = sant[0].lower()
if default == 'santos':
    print('O nome da cidade começa com SANTOS!')
else:
    print('O nome da cidade não começa com ')