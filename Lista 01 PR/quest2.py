import sys

print('Este programa simula um saque em caixa eletrônico.')

valor = float(input('Informe o valor a ser sacado em R$: '))

if valor <= 0:
    print('Deve ser escolhido um valor acima de zero!')
    sys.exit()


cem = valor // 100
valor -= cem * 100

cinquenta = valor // 50
valor -= cinquenta * 50

vinte = valor // 20
valor -= vinte * 20

dez = valor // 10
valor -= dez * 10

cinco = valor // 5
valor -= cinco * 5

dois = valor // 2
valor -= dois * 2

um = valor // 1 
valor -= um * 1 

cinquenta_cents = valor // 0.50
valor -= cinquenta_cents * 0.50

vinte_cinco = valor // 0.25
valor -= vinte_cinco * 0.25

dez_cents = valor // 0.10
valor -= dez_cents * 0.10

cinco_cents = valor // 0.5
valor -= cinco_cents * 0.5

um_cents = valor // 0.01
valor -= um_cents * 0.01
    
if cem > 0:
    print(f'{cem:.0f} cédula(s) de R$ 100,00.')
if cinquenta > 0:
    print(f'{cinquenta:.0f} cédula(s) de R$ 50,00.')
if vinte > 0:
    print(f'{vinte:.0f} cédula(s) de R$ 20,00.')
if dez > 0:
     print(f'{dez:.0f} cédula(s) de R$ 10,00.')
if cinco > 0:
    print(f'{cinco:.0f} cédula(s) de R$ 5,00.')
if dois > 0:
    print(f'{dois:.0f} cédula(s) de R$ 2,00.')
if um > 0:
    print(f'{um:.0f} moeda(s) de um R$ 1,00.')
if cinquenta_cents > 0:
    print(f'{cinquenta_cents:.0f} moeda(s) de R$ 0,50.')
if vinte_cinco > 0:
    print(f'{vinte_cinco:.0f} moeda(s) de R$ 0,25.')
if dez_cents > 0:
    print(f'{dez_cents:.0f} moeda(s) de R$ 0,10.')
if cinco_cents > 0:
    print(f'{cinco_cents:.0f} moeda(s) de R$ 0,05.')
if um_cents > 0:
    print(f'{um_cents:.0f} moeda(s) de R$ 0,01.')