# ** Gera um dict / * gera uma tupla


def resultado_f1(primeiro, segundo, terceiro):
    print(f'1- {primeiro}')
    print(f'2- {segundo}')
    print(f'3- {terceiro}')


if __name__ == '__main__':
    podium_2 = {'segundo': 'João de Deus',
                'primeiro': 'Galvão',
                'terceiro': 'Ronaldinho Preso',
                }
    resultado_f1(**podium_2))
