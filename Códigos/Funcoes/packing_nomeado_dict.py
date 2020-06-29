# ** Gera um dict / * gera uma tupla


def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='Lewis Hamilton',  # Packing
                 segundo='Rubinho Barrichelo',
                 terceiro='Jair Bolsonaro',
                 quarto='Felipe Massa',
                 quinto='Rubinho Denovo')


podium_2 = {'primeiro': 'Galvão',
            'segundo': 'João de Deus',
            'terceiro': 'Ronaldinho Preso',
            }

resultado_f1(**podium_2)  # Unpacking
