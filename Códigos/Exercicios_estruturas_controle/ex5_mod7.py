a = []
limite = 0
b = []

while limite < 5:
    a.append(float(input('Insira um numero: ')))
    limite = limite + 1

for numeros in a:
    if numeros % 2 != 0:
        continue
    b.append(numeros)
print(f'Existem {len(b)} numeros pares na lista {a}')
