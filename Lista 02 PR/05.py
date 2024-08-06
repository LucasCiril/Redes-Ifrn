import sys

val = int(input('Digite um número inteiro positivo: '))

if val <= 0: 
    print("O valor deve ser acima de zero!")
    sys.exit()
    
else:
    contdr = 0
    num = val
    
    while num > 0:
        num = num // 10
        contdr += 1
        
print(f'O valor informado possui {contdr} dígito(s).')