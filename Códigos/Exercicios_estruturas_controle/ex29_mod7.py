A = []

while len(A) < 6:
    A.append(int(input('Digite um número:')))

print(A)

A = tuple(A)
P = []
X = []

for numero in A:
    if numero % 2 == 0:
        P.append(numero)
    if numero % 2 != 0:
        X.append(numero)

print(f' Soma dos pares: {sum(P)}')
print(f'Números pares: {P}')
print(f'Números ímpares: {X}')
print(f'Quantidade de números ímpares: {len(X)}')
