import sys

print('Este programa calcula quantos dias se passaram entre duas datas. ')

dia_inicial = int(input('Digite o dia inicial: '))
mes_inicial = int(input('Digite o mês inicial: '))

dia_final = int(input('Digite o dia final: '))
mes_final = int(input('Digite o mês final: '))

if mes_inicial > mes_final or mes_inicial == mes_final and dia_inicial > dia_final:
    print('A Data Inicial não pode ser maior que a Data Final!')
    sys.exit()

dias_por_mes = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dias_totais_inicio = sum(dias_por_mes[:mes_inicial - 1]) + dia_inicial

# Conta o número de dias até a data final
dias_totais_final = sum(dias_por_mes[:mes_final - 1]) + dia_final

# Calcula o número de dias entre as datas
dias_entre_datas = dias_totais_final - dias_totais_inicio

print(f'Número de dias entre as datas: {dias_entre_datas:.0f}')