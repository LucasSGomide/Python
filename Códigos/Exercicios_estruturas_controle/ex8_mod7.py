a = []
contador = 0

while contador < 5:
    a.append(int(input('Digite um número: ')))
    contador = contador + 1
    continue

print(f'Ordem inversa = {a[::2]}')
