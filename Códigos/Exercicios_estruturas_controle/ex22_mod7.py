a = []
b = []
c = []
limite = 0
i = 0  # i = índice
A = 0
B = 0


while limite in range(0, 6):
    n = int(input('Digite um número: '))
    a.append(n)
    limite = limite + 1
    while limite in range(5, 10):
        n_2 = int(input('Digite outro número: '))
        b.append(n_2)
        limite = limite + 1
        if limite >= 10:
            while i in range(0, 10):
                if i % 2 == 0:
                    c.insert(i, a[A])
                    A = A + 1
                    i = i + 1
                else:
                    c.insert(i, b[B])
                    B = B + 1
                    i = i + 1
print(c)
