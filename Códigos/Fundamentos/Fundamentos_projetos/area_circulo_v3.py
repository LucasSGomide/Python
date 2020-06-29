#! python
from decimal import Decimal, getcontext
from math import pi

unidade = input('Informe a unidade: ')
raio = input('Informe o raio: ')
raio_2 = raio ** 2

getcontext().prec = 5

area = (Decimal(pi)) * (Decimal(raio_2))
print(f'Area: {area} {unidade}')
