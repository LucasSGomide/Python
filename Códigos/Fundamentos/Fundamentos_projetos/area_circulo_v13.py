#! python

from math import pi
import sys
import errno


def help():
    print('É necessário informar o raio do circulo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0]))


def circulo(raio):
    return (pi) * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        help()
        print('O raio tem que ser um valor numerico')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    raio = circulo(raio)
    print('Área do circulo:', raio)
