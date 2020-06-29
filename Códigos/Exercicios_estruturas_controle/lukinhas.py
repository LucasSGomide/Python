#!python

from collections import Counter


def criar_lista():
    lista = []
    limite = 0
    final = 0
    while limite < 10:
        lista.append(float(input('Insira um Número: ')))
        limite = limite + 1
        final = Counter(lista)
    for chave, valor in final.items():
        if valor > 1:
            for itens_chave in chave:
                print('Repetidos: ', itens_chave)
    else:
        print('Não existem valores repetidos.', lista)


if __name__ == '__main__':
    criar_lista()
