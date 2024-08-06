import sys

massa_inicial = float(input("Digite o valor inicial da massa em gramas: "))

if massa_inicial <= 0:
    print('O valor deve ser acima de zero!')
    sys.exit()
    
tempo_segundos = 0
massa_atual = massa_inicial

while massa_atual > 0.5:
    massa_atual /= 2
    tempo_segundos += 50
    
horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60

print(f"Massa inicial: {massa_inicial} gramas.")
print(f"Massa final: {massa_atual} gramas.")
print(f"Tempo de decaimento: {int(horas)}: {int(minutos):02}: {int(segundos):02}")    