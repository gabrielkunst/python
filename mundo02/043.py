"""  
1) O programa deve receber o peso e a altura de uma pessoa e retornar o IMC desta;
2)  Abaixo de 18.5 (abaixo do peso)
    Entre 18.5 e 25 (peso ideal)
    25 até 30 (sobrepeso)
    30 até 40 (obesidade)
    Acima de 40 (obesidade mórbida)
"""

print('Bom dia, seja bem vindo ao imccalc.online!')
weight = float(input('Qual é o seu peso em Kg?'))
height = float(input('Quantos metros você tem?'))
imc = weight/(height**2)

if imc < 18.5:
    print(f'Você está com IMC = {imc:.2f}, logo está abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print(f'Você está com IMC = {imc:.2f}, logo está com o peso ideal.')
elif 25 <= imc < 30:
    print(f'Você está com IMC = {imc:.2f}, logo está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Você está com IMC = {imc:.2f}, logo está com obesidade.')
else: 
    print(f'Você está com IMC = {imc:.2f}, logo está com obesidade mórbida. Tome mais cuidado!')