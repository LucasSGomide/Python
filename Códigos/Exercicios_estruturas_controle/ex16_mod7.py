import sys

a = []
fator = 0
limite = 0

while limite < 5:
    n = float(input('Digite um número: '))
    a.append(n)
    limite = limite + 1
    if limite >= 5:
        fator = int(input('Digite um fator: '))
        if fator == 0:
            sys.exit
        elif fator == 1:
            print(a)
        elif fator == 2:
            print(a[::-1])
        else:
            print('Código inválido (Sintaxe: fator 0, 1 ou 2)')
