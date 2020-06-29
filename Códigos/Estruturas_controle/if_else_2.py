#! python

import sys


def erro():
    print('Arquivo Incorreto')


def nota_invalida():
    print('Valor Inválido')
    print('Sintaxe: Números entre 0 e 10')


nota_input = (input('Informe a NOTA: '))
nota = nota_input

try:
    nota = int(nota_input)
except ValueError:
    try:
        nota = float(nota_input)
    except ValueError:
        nota_invalida()
        sys.exit(1)

if __name__ == '__main__':
    if nota > 10:
        nota_invalida()
        sys.exit(1)
    elif nota >= 9.1:
        print('A')
    elif nota >= 8.1:
        print('A-')
    elif nota >= 7.1:
        print('B')
    elif nota >= 6.1:
        print('B-')
    elif nota >= 5.1:
        print('C')
    elif nota >= 4.1:
        print('C-')
    elif nota >= 3.1:
        print('D')
    elif nota >= 2.1:
        print('D-')
    elif nota >= 1.1:
        print('E')
    elif nota >= 0:
        print('E-')
    else:
        nota_invalida()
else:
    erro()
