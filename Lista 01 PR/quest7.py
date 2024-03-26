import sys
import math

print('Este programa trabalha com informações sobre triângulos. ')

a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))

lados = a + b or a + c or b + c

if a > b + c or b > a + c or c > b + a:
    print('O trio de segmentos (lados) informados não satisfaz a condição de existência de um triângulo. ')
    sys.exit()

else:
    print('O trio de segmentos (lados) informados satisfaz a condição de existência de um triângulo. ')
    
angulo1 = math.degrees(math.acos((b**2 + c**2 - 2**a)/(2*b*c)))
angulo2 = math.degrees(math.acos((a**2 + c**2 - 2**b)/(2*a*c)))
angulo3 = 180 - angulo1 - angulo2

print('As medidas dos ângulos deste triângulo são: ')
print(f'{round(angulo1, 2)}°')
print(f'{round(angulo2, 2)}°')
print(f'{round(angulo3, 2)}°')

if a == b and b == c:
    print('Pelas informações dos lados, o triângulo formado será Equilátero.')
elif a == b or b == c:
    print('Pelas informações dos lados, o triângulo formado será Isósceles. ')
else:
    print('Pelas informações dos lados, o triângulo formado será Escaleno. ')
    
if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print('Pelas informações dos ângulos, o triângulo formado será Acutângulo. ')
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print('Pelas informações dos ângulos, o triângulo formado será Retângulo. ')
else:
    print('Pelas informações dos ângulos, o triângulo formado será Obtsusângulo. ')