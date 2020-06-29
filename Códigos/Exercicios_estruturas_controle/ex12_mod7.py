a = []
limite = 0

while limite < 5:
    a.append(float(input('Digite um número: ')))
    limite = limite + 1

print(f'''
Maior valor = {max(a, key = float)}
Menor valor = {min(a, key = float)}
Média = {sum(a) / len(a)}
''')
