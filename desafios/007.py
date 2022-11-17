name = str(input('Qual é o nome do aluno(a)?')).strip().title()
n1 = float(input(f'Qual foi a nota do(a) {name} na AV1?'))
n2 = float(input(f'Qual foi a nota do(a) {name} na AV2?'))
n3 = float(input(f'Qualf foi a nota do(a) {name} na AV3?'))
final = (n1+n2+n3)/3
print(f'A média final do(a) {name} foi {final:.2f}')
if final >= 60:
    print(f'Parabéns! O(a) {name} foi aprovado(a)!')
else:
    print(f'O(a) {name} foi reprovado(a). Deve estudar mais!')