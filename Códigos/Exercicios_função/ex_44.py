from random import choice

vetor = []
while len(vetor) < 30:
    vetor.append(choice(range(100)))


def vetor_aleatorio(vetor):
    pares = [pares for pares in vetor if pares % 2 == 0]
    impares = [impares for impares in vetor if impares % 2 != 0]
    print(f'Pares= {pares} Impares= {impares}')


vetor_aleatorio(vetor)
