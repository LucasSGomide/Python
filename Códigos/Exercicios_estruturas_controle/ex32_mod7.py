A = []
B = []
limite = 5

# Checagem de valores A

while len(A) < limite:
    a = (int(input('A: Informe um número: ')))
    if a not in A:
        A.append(a)
    else:
        print('Número inválido: <Sintaxe: N1 != N2>')

# Checagem de valores B

while len(B) < limite:
    b = (int(input('B: Informe um número: ')))
    if b not in B:
        B.append(b)
    else:
        print('Número inválido: <Sintaxe: N1 != N2>')

print(f'Lista A = {A}')
print(f'Lista B = {B}')

# Soma A[x] + B[x]

S = []
Aindice = 0
Bindice = 0

while len(S) < limite:
    S.append(A[Aindice] + B[Bindice])
    Aindice = Aindice + 1
    Bindice = Bindice + 1
print(f'Soma A[x] + B[x] = {S}')

# Produto A[x] * B[x]

P = []
Aindice = 0
Bindice = 0

while len(P) < limite:
    P.append(A[Aindice] * B[Bindice])
    Aindice = Aindice + 1
    Bindice = Bindice + 1
print(f'Produto A[x] * B[x] = {P}')

# Diferença, União e Interseção entre A e B:

num = 0
D = []

for num in A[:]:
    if num not in B:
        D.append(num)

num = 0

for num in B[:]:
    if num not in A:
        D.append(num)

A = set(A)
B = set(B)
inter = A.intersection(B)
uniao = A.union(B)

print(f'Diferença entre A e B = {D}')
print(f'Interseção entre A e B = {inter}')
print(f'União entre A e B = {uniao}')
