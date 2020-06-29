A = []
limite = 5

while len(A) < 5:
    a = int(input('Digite um número: '))
    if a not in A[:]:
        A.append(a)
    else:
        print(f'{a} É um número repetido !')

print('Lista:', A)
