def simplifica(valor, valor_2):
    divisor = valor - 1
    divisor_2 = valor_2 - 1
    reult = 0
    result_2 = 0
    while divisor != 0:
        if valor % divisor == 0:
            valor = valor / divisor
            reult = divisor
            divisor = 0
        else:
            divisor -= 1
    while divisor_2 != 0:
        if valor_2 % divisor_2 == 0:
            valor_2 = valor_2 / divisor_2
            result_2 = divisor_2
            divisor_2 = 0
        else:
            divisor_2 -= 1
    return(f'Maiores divisores: {reult}/{result_2}')


print(simplifica(418, 280))
