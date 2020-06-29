A = []
B = []
limite = 2

while len(A) < limite:
    a = int(input('Digite um número: '))
    if a < 0:
        print('Numero inválido')
    elif a > 10000:
        print('Numero inválido')
    else:
        A.append(a)
    for num in list(str(a)):
        B.append(int(num))

print('A =', A)
print("B =", B)

C = []
pos = 0

for num in B:  # Para os números em B
    if len(C) == 0:  # Se o comprimento de C == 0
        C.append(num)  # Adicionar o 1º numero
    elif len(C) == 1:  # Se comprimento de C == 1
        if num > C[pos]:  # Se numero maior que C[pos] == C[0]
            C.insert(pos + 1, num)  # Iserir numero (pos + 1) == C[1]
        else:  # Se não for maior
            C.insert(pos, num)  # Inserir em (pos) == C[0]
    else:  # Se o comprimento for maior que 1
        if C[len(C) - 1] < num:  # Se o último número adicionado menor que num
            C.insert(len(C), num)  # Inserir o num na última posição == len(C)
            pos = pos + 1  # Posição aumenta em 1 C[2]
        else:  # Se for maior
            while num > C[pos]:  # Enquanto o num for maior que C[2]
                pos = pos + 1  # 2 = 2 + 1 (conta posições)
            C.insert(pos, num)  # inserir numero no índice 3
            pos = 0

soma = (A[0] + A[1])

print('C = ', C)
print('Soma = ', soma)
