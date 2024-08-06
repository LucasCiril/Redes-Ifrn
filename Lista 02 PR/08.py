import sys

x1 = int(input('Digite um número: '))

n = 1
tri = n*(n+1) // 2

while  tri < x1:
    n += 1
    tri = n*(n+1) //2
    
if tri == x1:
    print(f'O número {x1} é triangular.')
    
else:
    print(f'O número {x1} não é triangular.')