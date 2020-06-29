from random import randint


def sorteio():
    return randint(1, 6)


sortear_dado = sorteio()

for dado in range(1, 7):
    if dado % 2 == 1:
        continue
    if dado == sortear_dado:
        print('Acertou ! Nº = ', dado, 'Nº Sorteado = ', sortear_dado)
        break
else:
    print('Errou, tente novamente', dado, 'Nº Sorteado = ', sortear_dado)
