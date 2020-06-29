a = []
limite = 0

while limite < 5:
    n = (float(input('Digite um valor: ')))
    limite = limite + 1
    if n < 0:
        a.append(0)
    else:
        a.append(n)

print(a)
