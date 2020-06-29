a = []
limite = 0

while limite < 5:
    n = float(input('Digite um valor: '))
    a.append(n)
    limite = limite + 1
    if a.count(n) > 1:
        a.remove(n)
print(a)
