lista = [0, 1, 2, 3, 4]

# 1º caso, printa do índice 0 até o indice 2.
# utilizado para escolher uma range específica
print(lista[0:3])

# 2º caso, printa do índice 0 até o 2
print(lista[:3])

# 3º Caso print do índice 1 até o -2
# Quando conta de trás pra frente índice -1 = 4 , -2 = 3..
print(lista[1:-2])

# 4º caso, printa do índice 0 em diante.
print(lista[0:])

# 5 º caso, pula sempre 1 número da lista
print(lista[::2])

# 6º caso, inverte a lista
print(lista[::-1])

# 7º caso, deleta toda a lista.
# del lista

# 8º caso, deleta um elemento da lista.
# del lista[1]

# 9º caso, deleta do índice 1 em diante.
# del lista[1:]

# 10º caso, soma os itens da lista
print(sum(lista))

print(lista[:])
