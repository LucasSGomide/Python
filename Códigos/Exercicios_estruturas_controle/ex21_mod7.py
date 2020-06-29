a = []
b = []

limite = 0

while limite < 5:
    n_1 = int(input('Insira um número: '))
    a.append(n_1)
    limite = limite + 1
    if limite >= 5:
        while limite < 10:
            n_2 = int(input('(2) Insira um número: '))
            b.append(n_2)
            limite = limite + 1
            if limite >= 10:
                c = list(set(a) - set(b))

print(f'Lista A = {a} - lista B {b} = {c}')
