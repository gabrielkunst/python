"""  
1) O programa deve receber as notas de um aluno e calcular a média;
2) Uso de condições 
3) Média >= 70 (aprovado), 5.0 < média < 6.9 (em recuperação) ou média < 5 (reprovado).
"""

print('Bom dia, tudo bem?')
q1 = int(input('Quanto o aluno tirou no primeiro trimestre?'))
q2 = int(input('Quanto o aluno tirou no segundo trimestre?'))
q3 = int(input('Quanto o aluno tirou no terceiro trimestre?'))
av = (q1 + q2 + q3)/3
if av >= 70:
    print(f'O aluno ficou com média {av:.0f}, logo foi \033[1;32maprovado!\033[m')
elif 50 <= av <= 69:
    print(f'O aluno ficou com média {av:.0f}, logo ficou \033[1;33mem recuperação!\033[m')
else:
    print(f'O aluno ficou com média {av:.0f}, logo foi \033[1;31mreprovado!\033[m')