from math import pi


def volume_cilinro(altura, raio):
    v = pi * raio ** raio * altura
    return(f'Volume do cilindro é {round(v, 2)}m³')


print(volume_cilinro(1, 0.5))
