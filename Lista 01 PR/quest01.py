import sys

print('Este programa calcula a soma de um algarismo entre 0 e 9999. ')

x = int(input('Digite o algarismo: '))

if x < 0 or x > 9999:
    print('Número inválido para este programa.')
    sys.exit()
    
unidade = x // 1 % 10
dezena = x // 10 % 10
centena = x // 100 % 10
milhar = x // 1000 % 10

algarismo = unidade + dezena + centena + milhar

print(f'O resultado da soma dos algarismos do número digitado é: {algarismo} ')