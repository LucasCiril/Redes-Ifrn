import sys


n1 = int(input('Informe o primeiro número inteiro positivo: '))
n2 = int(input('Informe o segundo número inteiro positivo: '))

if n1 <= 0 or n2 <= 0:
    print('Os números devem ser positivos inteiros!')
    sys.exit()
    
else:
    while n2 != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto
        
print(f'O máximo divisor comuum entre os números é: {n1}')