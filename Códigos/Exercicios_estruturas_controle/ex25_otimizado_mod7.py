a = []
contador = 0
fator = 7

while len(a) < 100:
    if contador % 10 == 0:  # se for múltiplo de 10
        fator = contador + 7  # fator será 7 + contador(multiplo de 10)
        contador = contador + 1  # pula a contagem e boa.
    elif fator == contador:
        contador = contador + 1
    elif contador % 7 != 0:
        a.append(contador)
        contador = contador + 1
    else:
        contador = contador + 1
print(a)
