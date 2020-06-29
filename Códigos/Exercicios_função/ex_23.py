def desenho_linhas(valor):
    mult = 0
    mult_2 = valor
    cont = 0
    limite = 2 * valor - 1
    for n in range(1, 2 * valor):
        while cont <= limite:
            if mult <= valor:
                mult += n
                cont += 1
                print('*' * mult)
            elif mult >= valor:
                mult_2 -= n
                cont += 1
                print('*' * mult_2)


(desenho_linhas(10))
