import sys

vli = int(input('Digite o valor incial da P.G: '))
raz = int(input('Digite o valor da razão da P.G: '))

if raz == 0:
    print('O valor da razão não pode ser zero!')
    sys.exit()
    
qnt_el = int(input('Insira a quantidade de elementos da P.G: '))

pg = [vli * (raz ** i) for i in range(qnt_el)]

print('Os elementos da P.G são estes: ')

for valor in pg:
    print(valor)
    
if all(x == pg[0] for x in pg):
    tipo_pg = "Constante"
    
elif all(pg[i] < pg[i + 1] for i in range(len(pg) - 1)):
    tipo_pg = "Crescente"
    
elif all(pg[i] > pg[i + 1] for i in range(len(pg) - 1)):
    tipo_pg = "Decrescente"
    
else:
    tipo_pg = "Oscilante"

print(f"A P.G. é {tipo_pg}.")

soma_pg = sum(pg)
print(f"A soma dos elementos da P.G. é: {soma_pg}")

n = int(input("Digite a posição (n) para encontrar o valor da P.G.: "))
if n <= qnt_el and n > 0:
    valor_enesimo = vli * (raz ** (n - 1))
    print(f"O valor do elemento na posição {n} é: {valor_enesimo}")
else:
    print("Posição inválida. Certifique-se de que o valor está dentro do intervalo da quantidade de elementos.")