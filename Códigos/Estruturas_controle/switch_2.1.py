#! python


def tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana'
    }
    return dias.get(dia, '** dia inválido **')


if __name__ == '__main__':
    for dias in range(9):
        print(f'Hoje é o dia {dias} e este é um {tipo_dia(dias)}')

# def (nome) 'tipo_dia' (parâmetro) ('dia'):
# 'dias' é o nome do dicionário, 1(dia), 2(dia), 3(dia) - dia == função
# return retornará um valor dias.get(dia) + 'mensagem default'
