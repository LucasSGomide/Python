A = []
P = []

while len(A) < 5:
    A.append(int(input('Digite um número: ')))
print(A)

primo = 0
a = 0
num = 1

while a < len(A):
    while num in range(1, A[a] + 1):
        if A[a] % num == 0:
            primo = primo + 1
            num = num + 1
        else:
            num = num + 1
    if primo == 2:
        P.append(A[a])
        a = a + 1
        num = 1
        primo = 0
    else:
        a = a + 1
        num = 1
        primo = 0

print(P)

for k, v in enumerate(P):
    print(k, v)
