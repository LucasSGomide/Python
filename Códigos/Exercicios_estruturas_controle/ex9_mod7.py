a = []
contador = 0

while contador < 5:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        a.append(n)
        contador = contador + 1
    continue
print(a[::-1])
