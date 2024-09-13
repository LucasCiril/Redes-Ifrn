import requests, sys
import json
import os
import matplotlib.pyplot as plt
from datetime import *

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&'
strURL += f'@dataFinalCotacao=%2712-31-2023%27&$format=json'
dictCotacoes = requests.get(strURL).json()

ano_at = date.today().year

while True:
    try:
        ano = int(input('\n' f'Informe o ano desejado, que não seja superior à {ano_at}: '))
        if ano > ano_at:
            print('\n', f'Ano não pode ser superior à {ano_at}. Por favor, repita a operação.')
        else:
            print('\n', 'Ano válido. Próximo passo:')
            break   
    except ValueError:
        print('\n', 'Por favor, digite um ano válido.')
        break

moedasval = [moeda['simbolo'] for moeda in dictMoedas['value']]

while True:
        moeda = input('\n' f"Digite a sigla da moeda desejada (moedas válidas: {', '.join(moedasval)}): ").strip().upper()
        if moeda in moedasval:
            print('\n' f'A moeda escolhida foi: {moeda}')
            break
        else:
            print('\n' 'Sigla inválida. Tente novamente.')
            break

mesnom = {
    '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
    '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
    '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
}
mediamensal = {}

for cotacao in dictCotacoes['value']:
    data = cotacao['dataHoraCotacao'].split('T')[0]
    mes = data[5:7]
    if mes not in mediamensal:
        mediamensal[mes] = {'mediaCompra': [], 'mediaVenda': []}
    if cotacao['cotacaoCompra'] is not None and cotacao['cotacaoVenda'] is not None:
        mediamensal[mes]['mediaCompra'].append(cotacao['cotacaoCompra'])
        mediamensal[mes]['mediaVenda'].append(cotacao['cotacaoVenda'])
        

medias_calculadas = {}
for mes in mediamensal:
    if mediamensal[mes]['mediaCompra'] and mediamensal[mes]['mediaVenda']:
        mediaCompra = sum(mediamensal[mes]['mediaCompra']) / len(mediamensal[mes]['mediaCompra'])
        mediaVenda = sum(mediamensal[mes]['mediaVenda']) / len(mediamensal[mes]['mediaVenda'])
        medias_calculadas[mes] = {
            'mediaCompra': round(mediaCompra, 5),
            'mediaVenda': round(mediaVenda, 5)
        }
    else:
        print(f"Sem dados suficientes para o mês {mesnom[mes]}.")

nome_arquivo_json = f'medias_cotacoes_{moeda}_{ano}.json'
nome_arquivo_csv = f'medias_cotacoes_{moeda}_{ano}.csv'

if os.path.exists(nome_arquivo_json):
    print(f"Atenção: O arquivo {nome_arquivo_json} já existe e será sobrescrito.")
if os.path.exists(nome_arquivo_csv):
    print(f"Atenção: O arquivo {nome_arquivo_csv} já existe e será sobrescrito.")

try:
    with open(nome_arquivo_json, 'w') as json_file:
        json.dump(medias_calculadas, json_file, indent=4)
except IOError as e:
    print(f"Erro ao salvar o arquivo JSON: {e}")
    exit()
    
    
try:
    with open(nome_arquivo_csv, 'w') as csv_file:
        csv_file.write('moeda;mes;mediaCompra;mediaVenda\n')
        for mes in medias_calculadas:
            mes_nome = mesnom[mes]
            csv_file.write(f'{moeda};{mes_nome};{medias_calculadas[mes]["mediaCompra"]:.5f};{medias_calculadas[mes]["mediaVenda"]:.5f}\n')
except IOError as e:
    print(f"Erro ao salvar o arquivo CSV: {e}")
    exit()
    
#Bônus:
  
meses = [mesnom[mes] for mes in medias_calculadas]
media_compra = [medias_calculadas[mes]['mediaCompra'] for mes in medias_calculadas]
media_venda = [medias_calculadas[mes]['mediaVenda'] for mes in medias_calculadas]

plt.figure(figsize=(10, 6))  
plt.plot(meses, media_compra, label='Média Compra', marker='o') 
plt.plot(meses, media_venda, label='Média Venda', marker='o')
plt.title(f'Média Cotações {moeda} – Ano {ano}')
plt.xlabel('Mês')
plt.ylabel('Cotação')
plt.xticks(rotation=45)  
plt.legend()  
plt.tight_layout() 
plt.show()  

print("Eis o gráfico.")