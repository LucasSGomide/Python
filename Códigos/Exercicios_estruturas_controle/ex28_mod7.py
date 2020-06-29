A = []

while len(A) < 5:
    a = (int(input('Insira um valor: ')))
    if a >= 0:
        A.append(a)
    else:
        print('Erro de sintaxe. <Inteiros >= 0>')

print(A)

A = tuple(A)
Im = []
P = []

for num in A:
    if num % 2 == 0:
        P.append(num)
    else:
        Im.append(num)

print(f'Lista de pares: {P}')
print(f'Lista de ímpares: {Im}')
