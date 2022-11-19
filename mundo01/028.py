""" 
O COMPUTADOR DEVE PENSAR EM UM NÚMERO ENTRE 0 E 5 E PEDIR PARA O USUÁRIO DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO. DEVE-SE USAR IF PARA MOSTRAR O RESULTADO AO USUÁRIO.
1) O PC DEVE ESCOLHER UM NÚMERO
2) PEDIR PARA O USUÁRIO QUAL FOI O NÚMERO ESCOLHIDO
3) RETORNAR AO USUÁRIO A RESPOSTA.
4) Pode até colocar um time.sleep() para ficar mais legal.
"""
import random
num = random.randrange(6)
print('O sistema escolheu um valor.')
usernum = int(input('Qual foi o valor escolhido pelo sistema?'))
if usernum == num:
    print(f'Wowww, o valor escolhido foi {num} e você acertou, parabéns!')
else:
    print(f'O valor escolhido foi {num}, mas você escolheu {usernum}. Tente novamente!')
 