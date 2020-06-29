# Variaveis

A = []
limite = 5

# Recebendo os valores

while len(A) < limite:
    A.append(float(input('Digite um número: ')))

# Novas variaveis

pos = 0
B = []

# Ordenando os valores

for num in A:
    if len(B) == 0:
        B.append(num)
    elif len(B) == 1:
        if num > B[len(B) - 1]:
            B.insert(pos + 1, num)
        else:
            B.insert(pos, num)
    else:
        if num > B[len(B) - 1]:
            B.insert(len(B), num)
            pos = pos + 1
        else:
            while num > B[pos]:
                pos = pos + 1
            B.insert(pos, num)
            pos = 0

print('A = ', A)
print('B = ', B)
