import sys

lista_vazia = []

x = int(input('Informe a quantidade de elementos positivos na lista: '))

while True:
    n = int(input('Digite um valor inteiro: '))
    lista_vazia.append(n)
    lista_vazia2 = sorted(lista_vazia)
    print(lista_vazia2)
    
    if n == 0:
        break
    

    
if len(lista_vazia2) > x:
    lista_vazia2 = lista_vazia2[:x]
    
print(f'Lista: {lista_vazia2}')