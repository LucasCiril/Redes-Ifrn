import random
import math

n = int(input('Digite um valor: '))

while n <= 0:
    n = int(input('Valor inválido! Digite um número positivo: '))

lista = [random.randint(0,99) for i in range(n)]

soma = sum(lista)
media = soma / n

lista_ord = sorted(lista)
if n % 2 == 1:
    mediana = lista_ord[n // 2]

else:
    mediana = (lista_ord[n // 2 - 1] + lista_ord[n // 2]) / 2

soma_qd = sum([(x - media) ** 2 for x in lista])
varia = soma_qd / n

desv = math.sqrt(varia)

print(f'Lista gerada: {lista}')
print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Variância: {varia:.2f}')
print(f'Desvio-padrão populacional: {desv:.2f}')