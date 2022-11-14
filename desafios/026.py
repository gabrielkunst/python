""" 
O PROGRAMA DEVE LER UMA FRASE DEFINIDA PELO USUÁRIO E DEVE CONTAR O NÚMERO DE "A" E AONDE ESTE APARECE.
- Defini um padrão entre a frase e a letra, ou seja, tudo minúsculo, depois o algoritmo faz a contagem da letra definida e por último define a primeira e última posição. 

"""

ph = input('Digite uma frase:')
phlow = ph.lower()
print(f"A sua frase possui: {phlow.count('a')} letras 'a'.")
print(f"A primeira letra 'a' aparece na posição {phlow.find('a')}.")
print(f"A última letra 'a' aparece na posição {phlow.rfind('a')}")