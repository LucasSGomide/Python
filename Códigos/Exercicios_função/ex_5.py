from math import pi


def volume_esfera(raio):
    v = 4 / 3 * pi * raio
    return round(v, 2)


print(volume_esfera(10))
