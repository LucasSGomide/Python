#! python

from math import pi
from decimal import Decimal, getcontext

unidade = input('Informe a unidade: ')
raio = input('Informe o raio: ')
raio_2 = float(raio) ** 2

getcontext().prec = 5

area = (Decimal(pi)) * (Decimal(raio_2))
print(f'Area: {area} {unidade}')
