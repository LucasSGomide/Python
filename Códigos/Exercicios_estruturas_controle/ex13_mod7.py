a = []
limite = 0

while limite < 5:
    a.append(float(input('Digite um número: ')))
    limite = limite + 1

maior = max(a, key=float)
menor = min(a, key=float)

print(f'''
Posição do maior valor = {a.index(maior)}
Posição do menor valor = {a.index(menor)}
''')
