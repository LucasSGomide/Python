from random import choice


def vetor_aleatorio(vetor=[]):
    vetor = []
    while len(vetor) < 10:
        vetor.append(choice(range(100)))
    return(vetor)


vetor_aleatorio()
