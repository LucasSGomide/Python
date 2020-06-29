

def funcao(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        tuple(range(2, 7)): 'Dia de Semana',
    }
    generator = (a for a in range(8))
    for dados in generator:
        if dados == dia:
            for chave, valor in dias.items():
                if dados in chave:
                    print(f'{dia} e {valor}')
    if dia >= 8:
        print(f'Dia invalido {dia}')


if __name__ == '__main__':
    funcao(6)
