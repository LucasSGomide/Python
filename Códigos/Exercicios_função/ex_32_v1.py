def simplifica(valor_1, valor_2):
    valor = valor_1 > valor_2
    if valor is True:
        divisor = valor_1 - 1
    else:
        divisor = valor_2 - 1
        while divisor > 0:
            if valor_1 % divisor == 0 and valor_2 % divisor == 0:
                valor_1 = valor_1 / divisor
                valor_2 = valor_2 / divisor
                divisor = 0
                return(f'Fracao simplificada: {valor_1}/{valor_2}')
            else:
                divisor -= 1


print(simplifica(90, 123))
