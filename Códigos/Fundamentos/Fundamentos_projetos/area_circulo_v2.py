# -*- coding: utf-8 -*-
from decimal import Decimal, getcontext

unidade = 'm²'
pi = 3.14159
raio = 15.3
raio_2 = raio ** 2

getcontext().prec = 5

area = (Decimal(pi)) * (Decimal(raio_2))
print(f'Area: {area} {unidade}')
