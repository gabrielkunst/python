"""  
Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

print('Bem vindo ao conversor.net!')
m = float(input('Quantos metros você deseja converter?'))

mm = m*1000
cm = m*100
dm = m*10
dam = m/(10)
hm = m/(100)
km = m/(1000)

print(f'{m} metros é igual a {mm}mm, {cm}cm, {dm}dm, {dam}dam, {hm}hm e {km}km.')
