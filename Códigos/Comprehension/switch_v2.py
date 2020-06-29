

def funcao(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        tuple(range(2, 7)): 'Dia de Semana',
    }
    generator = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(generator, '** dia invalido **')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {funcao(dia)}')
