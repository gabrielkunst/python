print('Bom dia, seja bem vindo ao temper.net!')
degree = input('Qual sua métrica de medida inicial, C (celsius) ou F (fahrenheit)?')
num = float(input('Informe a temperatura:'))
cf = (num * (9/5) + 32)
fc = ((num - 32) * (5/9))

if degree == "C":
    print(f'A medida escolhida foi Celsius. {num:.2f}C é igual a {cf:.2F}F.')
else:
    print(f'A medida escolhida foi Fahrenheit. {num:.2f}F é igual a {fc:.2F}C.')