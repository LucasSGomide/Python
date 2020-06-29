A = []
B = []

while len(A) < 5:
    A.append(int(input('Informe um número: ')))

while len(B) < 5:
    B.append(int(input('Informe um número: ')))

A = set(A)
B = set(B)
C = (A.union(B))

print(C)
