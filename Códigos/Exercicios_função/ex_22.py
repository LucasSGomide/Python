def desenho_linhas(valor):
    mult = 0
    for n in range(1, valor + 1):
        while mult <= valor:
            if mult <= valor:
                mult += n
                print('!' * mult)


(desenho_linhas(10))
