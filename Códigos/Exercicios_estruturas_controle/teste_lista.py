A = []
negativos = 0
cont = 0
soma_positivos = 0

# Preenchendo vetor
while cont < 5:
    A.append(float(input('Digite um valor: ')))
    cont = cont + 1

print(A)

# Calculando números negativos
cont = 0
while cont < 5:
    if A[cont] < 0:
        negativos = negativos + 1
        cont = cont + 1
    else:
        soma_positivos = soma_positivos + A[cont]
        cont = cont + 1

print(f'A quantidade de números negativos nesse vetor é {negativos}.')
print(f'A soma dos números pares do vetor é {soma_positivos}.')
