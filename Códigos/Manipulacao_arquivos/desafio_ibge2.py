import csv

with open('desafio_ibge.csv') as entrada:
    with open('desafio_ibge.txt', 'w') as saida:
        leitor = csv.DictReader(entrada)  # Entrada vira um dict ordenado
        for coluna in leitor:
            coluna1 = coluna['nome_orige']
            coluna9 = coluna['nome_desti']
            print(f'Coluna 1: {coluna1}, Coluna 9: {coluna9}', file=saida)
