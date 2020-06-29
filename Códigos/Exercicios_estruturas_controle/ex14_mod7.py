from collections import Counter

a = []
limite = 0

while limite < 5:
    n = (float(input('Digite um número: ')))
    a.append(n)
    limite = limite + 1

dicionario = (Counter(a))

for chave, valor in dicionario.items():
    if valor > 1:
        print(f'O numero {chave} repetiu {valor} vezes')
