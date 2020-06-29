def executar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom Dia !')


def boa_tarde():
    print('Boa Tarde')


executar(boa_tarde)
