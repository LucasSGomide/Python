a = []
b = []
limite = 0

while limite < 5:
    n = int(input('Digite um número: '))
    if n in range(0, 51):
        a.append(n)
        limite = limite + 1
        if n % 2 == 0:
            continue
        b.append(n)
    else:
        print('Erro ! (Sintaxe: 0 >= número <= 50)')

print(a)
print(b)
