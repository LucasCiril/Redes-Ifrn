import sys

xandao = int(input('Digite um número inteiro positivo: '))

if xandao < 99:
    print('O número deve conter, mo mínimo, três ou mais dígitos.')
    sys.exit()
    
xandao_org = xandao
soma_bill = 0
magnus = xandao
quant_magnus = 0

while magnus > 0:
    quant_magnus += 1
    magnus //= 10
    
magnus = xandao

while magnus > 0:
    sucumba = magnus % 10
    soma_bill += sucumba ** quant_magnus
    magnus //= 10
    
if soma_bill == xandao:
    print(f'O número {xandao} é um número de Armstrong.')
    
else:
    print(f'O número {xandao} não é um número de Armstrong.')