import random

linhas = int(input('Informe o número de linhas da matriz: '))
coluna = int(input('Informe o número de colunas da matriz: '))

matriz = [[random.randint(0, 9) for i in range(coluna)] for i in range(linhas)]

print("Matriz original: ")

for l in matriz:
    print(l)
    
mattriz = [[matriz[j][i] for j in range(linhas)] for i in range(coluna)]

print("Matriz Transposta: ")
for l in mattriz:
    print(l)
    
