import csv

with open('desafio_ibge.csv') as entrada:
    leitor = csv.reader(entrada)
    for coluna in leitor:
        print(f'{coluna[3]}: {coluna[8]}')
