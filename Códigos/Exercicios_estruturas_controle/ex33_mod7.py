A = []
limite = 5
num = 0

while len(A) < limite:
    A.append(int(input('Digite um número: ')))

for num in A[:]:
    if num == 0:
        A.remove(num)

print(A)
