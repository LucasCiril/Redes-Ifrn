import subprocess
import re

host = input("Digite o nome da máquina de destino (HOST): ")

strCMD = f'tracert -d4 {host}'
resultado = subprocess.run(strCMD, capture_output=True, text=True, shell=True)
conteudo = resultado.stdout

with open('rastreio.txt', 'w') as arquivo:
    arquivo.write(conteudo)

padrao_tempo = re.compile(r'(\d+)\s+ms\s+(\d+)\s+ms\s+(\d+)\s+ms')

tempos_minimos = {}
linhas = conteudo.split('\r\n')

for linha in linhas:
    partes = linha.split()
    if partes and partes[0].isdigit():
        numero_salto = int(partes[0])
        if numero_salto not in tempos_minimos:
            tempos_minimos[numero_salto] = []

        tempos = padrao_tempo.findall(linha)
        if tempos:
            tempos = [int(t) for sublist in tempos for t in sublist]
            tempos_minimos[numero_salto].extend(tempos)

tempos_minimos = {salto: min(tempos) for salto, tempos in tempos_minimos.items() if tempos}

print("Menor tempo de resposta para cada máquina:")
for salto, tempo in tempos_minimos.items():
    print(f"Salto {salto}: {tempo} ms")