
from random import choice

vetor = []
while len(vetor) < 5:
    vetor.append(choice(range(100)))


def programa(vetor):
    print(vetor)
    print(vetor[::-1])
    soma = sum(vetor)
    print(soma / len(vetor))


programa(vetor)