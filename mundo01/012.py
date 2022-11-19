v = float(input('Qual é o valor do produto?'))
dp = float(input('Quantos porcento de desconto será aplicado?'))
dd = dp/(100)
print(f'O valor final do produto será: {v-(v*dd):.2f}')