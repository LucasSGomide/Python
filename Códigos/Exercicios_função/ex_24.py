def desenho_linhas(valor):
    cont = 0
    limite = 2 * valor - 1
    ajuste = valor * 4
    conteudo = []
    while cont <= limite:
        conteudo.append('*')
        string = ' '.join(conteudo)
        print((string.center(ajuste)))
        cont += 1


(desenho_linhas(3))
