a = []
limite = 0
fator = 0

while limite < 5:
    n = int(input('Digite um numero: '))
    a.append(n)
    limite = limite + 1
    if limite >= 5:
        fator = int(input('Digite outro número: '))
        for multiplos in a:
            if multiplos % fator == 0:
                continue
        for n_multiplos in a:
            if n_multiplos % fator != 0:
                continue

print(f'Estes números {multiplos} são múltiplos de {fator}')
print(f'Estes números {n_multiplos} não são múltiplos de {fator}')
