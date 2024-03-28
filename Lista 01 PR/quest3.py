import sys

print('Computador de bordo, ativado.')

hr_partida = int(input('Hora da partida (0-23): '))
min_partida = int(input('Minuto da partida (0-59): '))
hr_chegada = int(input('Hora da chegada (0-23): '))
min_chegada = int(input('Minuto da chegada (0-59): '))
segundos_descanso = int(input('Segundos parados para descanso: '))
litros_gastos = float(input('Combustível gasto (em litros): '))
preco_litro = float(input('Preço do litro de combustível (em R$): '))
distancia = float(input('Distância percorrida (em Km): '))


#Tempo da viagem em segundos:
hr1 = (hr_chegada - hr_partida) *60
hr2 = hr1 *60

min1 = (min_chegada - min_partida) *60


just = hr2 + min1
tempo_total = just + segundos_descanso

trs1 = segundos_descanso / 60
trs2 = trs1 / 60

#Velocidade média:
vel_global = distancia / (trs2+ (hr_chegada - hr_partida)) 
vel_med_mov = distancia / (hr_chegada - hr_partida) 

#Gasto com combustível:
custo_combustivel = litros_gastos * preco_litro

#Desempenho do carro
desempenho_km_litro = distancia / litros_gastos
desempenho_litros_horas = litros_gastos / (tempo_total / 3600)
custo_km = litros_gastos / distancia

print('Dados do computador de Bordo:')
print(f'Tempo de viagem: {tempo_total:.0f} segundos.')
print(f'Velocidade média global: {vel_global:.2f} Km/h')
print(f'Velocidade média em movimento: {vel_med_mov:.2f} Km/h')
print(f'Custo da viagem com combustível: R$ {custo_combustivel:.2f}')
print('Desempenho do carro:')
print(f'  - Consumo médio: {desempenho_km_litro:.2f} l/h')
print(f'  - Consumo médio de combustível: {desempenho_litros_horas:.2f} l/f')
print(f'  - Custo por Km: R$ {custo_km:.2f} /Km')