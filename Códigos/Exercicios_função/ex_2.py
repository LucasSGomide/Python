def data_conversor(dia, mes, ano):
    meses = {
            1: 'janeiro',
            2: 'fevereiro',
            }
    for numero, extenso in meses.items():
        if mes == numero:
            return(f'Hoje é {dia} de {extenso} de {ano}')
        else:
            return(f'Mês {mes} é um valor inválido')


print(data_conversor(10, 3, 2020))
