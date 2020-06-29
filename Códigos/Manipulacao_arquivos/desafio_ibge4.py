import csv
from urllib import request


def ibge_down(url):
    with request.urlopen(url) as entrada:
        dados = entrada.read().decode('latin1')
        for cidade in csv.reader(dados.splitlines()):
            # splitlines separa as strings em lista
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == "__main__":
    ibge_down(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
