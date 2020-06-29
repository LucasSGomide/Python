#! python
"""
for i in range(1, 10):
    print(i)
else:
    print(fim!)
"""

# Desafio - minha resposta !

from random import randint

# def sorteio():
#    return randint(1, 6)

# sortear_dado = randint(1, 6)


def sorteio():
    return randint(1, 6)


sortear_dado = sorteio()

print(f'Sorteado = {sortear_dado}')

for dado in range(1, 7):
    if dado % 2 != 0:
        continue
    if dado == sortear_dado:
        print(f'Acertou = {dado}')
        break
else:
    print(f'Errou = {dado}')
