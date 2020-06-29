# dicionario = {chave: valor for item in list if condicional}

A = {i: i * 2 for i in range(10) if i % 2 == 0}
print(A)

# A = {f'Indice : {i}': i * 2 for i in range(10) if i % 2 == 0}
# print(A)

for numero, dobro in A.items():
    print(f'Numero: {numero} Dobro: {dobro}')
