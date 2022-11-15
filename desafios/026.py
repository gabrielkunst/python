""" 
O PROGRAMA DEVE LER UMA FRASE DEFINIDA PELO USUÁRIO E DEVE CONTAR O NÚMERO DE "A" E AONDE ESTE APARECE.
"""

ph = str(input('Digite uma frase:')).strip()
phlow = ph.lower()
print(f"A sua frase possui: {phlow.count('a')} letras 'a'.")
print(f"A primeira letra 'a' aparece na posição {phlow.find('a')+1}.")
print(f"A última letra 'a' aparece na posição {phlow.rfind('a')+1 }")