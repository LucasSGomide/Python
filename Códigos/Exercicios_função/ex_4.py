def raiz_perfeita(num):
    raiz = num ** 0.5  # raiz ex: 16 ** 0.5 = 4
    if raiz % 2 == 0:  # Definindo se raiz é int
        return(f'{num} é quadrado perfeito de {raiz}')
    elif raiz % 2 == 1:  # Definindo se raiz é int
        return(f'{num} é quadrado perfeito de {raiz}')
    else:  # Se não for, não é um quadrado perfeito.
        return(f'{num} Não é um quadrado perfeito')


print(raiz_perfeita(60))
