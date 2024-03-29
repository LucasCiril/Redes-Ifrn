from datetime import datetime, timedelta
import sys

print('Este programa calcula a idade que você poderá se aposentar. ')

sexo = input('Informe o sexo BIOLÓGICO (masculino/feminino): ')

if sexo == 'masculino':
    idade_aposentadoria = 65
    tempo_aposentadoria = 35
elif sexo == 'feminino':
    idade_aposentadoria = 62
    tempo_aposentadoria = 30
else:
    print('Sexo inválido. Favor, inserir masculino ou feminino. ')
    sys.exit()

#Data de Nascimento.
dt_nascimento = input('Informe a data do seu nascimento (DD/MM/AAAA): ')
dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y')

#Início da contribuição.
dt_inicio_contrib = input('Informe a data de início de sua contribuição (DD/MM/AAAA): ')
dt_inicio_contrib = datetime.strptime(dt_inicio_contrib, '%d/%m/%Y')


idade_atual = datetime.now().year - dt_nascimento.year
tempo_contrib = (datetime.now() - dt_inicio_contrib).days / 365

if idade_atual >= idade_aposentadoria and tempo_contrib >= tempo_aposentadoria:
    print('Você pode se aposentar.')
else:
    dt_aposentadoria_idade = dt_nascimento + timedelta(days=idade_aposentadoria*365)
    dt_aposentadoria_contrib = dt_inicio_contrib + timedelta(days=tempo_aposentadoria*365)
    dt_aposentadoria = max (dt_aposentadoria_idade, dt_aposentadoria_contrib)
    print(f'Você poderá se aposentar em {dt_aposentadoria.strftime('%d/%m/%Y')}.')
    print(f'Você tem {idade_atual} anos.')
