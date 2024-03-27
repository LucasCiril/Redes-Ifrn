import sys

print('Este programa calcula o preço a ser pago pelo estacionamento do seu carro. ')

minutos = float(input('Digite o número de minutos em que o carro ficou estacionado: '))

if minutos >= 720:
    print('O valor a ser pago é de 30,00 R$')
    sys.exit()

if minutos <= 60:
    print('O valor a ser pago é de: 8,00 R$')
elif minutos <= 120:
    print('O valor a ser pago é de: 16,00 R$')
elif minutos <= 180:
    print('O valor a ser pago é de: 21,00 R$')
elif minutos <= 240:
    print('O valor a ser pago é de: 26,00 R$ ')
elif minutos <= 300:
    print('O valor a ser pago é de: 29,00 R$ ')
elif minutos <= 360:
    print('O valor a ser pago é de: 32,00 R$')
elif minutos <= 420:
    print('O valor a ser pago é de: 35,00 R$')
elif minutos <= 480:
    print('O valor a ser pago é de: 38,00 R$')
elif minutos <= 540:
    print('O valor a ser pago é de: 41,00 R$')
elif minutos <= 600:
    print('O valor a ser pago é de: 44,00 R$')
else:
    print('O valor a ser pago é de: 47,00 R$')
