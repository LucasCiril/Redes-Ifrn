import sys
varus = int(input('Insira o valor inicial da P.A: '))
ashe = int(input('Insira a razão da P.A: '))

adcs = int(input('Insira a quantidade de elementos da P.A: '))

titan = [varus + i * ashe for i in range (adcs)]

for gap in titan:
    print(gap, end='' '')
print()

if ashe == 0:
    print("A P.A é constante.")
elif ashe > 0:
    print("A P.A é crescente.")
else:
    print("A P.A é decrescente.") 

posicao = int(input("Digite a posição (n) do elemento da P.A. que você deseja ver: "))

# Exibe o valor do elemento da P.A. na posição especificada
if 1 <= posicao <= adcs:
    valor_elemento = varus+ (posicao - 1) * ashe
    print(f"O valor do elemento na posição {posicao} é: {valor_elemento}")
else:
    print("A posição informada está fora do intervalo da Progressão Aritmética.")