a = []
contador = 0
proibidos = (17, 27, 37, 47, 57, 67, 77, 87, 97)

while contador in range(0, 100):
    if contador in proibidos:
        contador = contador + 1
    elif contador % 7 != 0:
        a.append(contador)
        contador = contador + 1
    else:
        contador = contador + 1
print(a)
