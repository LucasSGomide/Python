a = []
limite = 0
cont_neg = 0
soma_positivo = 0

while limite < 5:
    x = float(input('Informe um número: '))
    a.append(x)
    if x < 0:
        cont_neg = cont_neg + 1
        limite = limite + 1
    else:
        soma_positivo = soma_positivo + a[limite]
        limite = limite + 1

print(f'Sua lista tem {cont_neg} números negativos')
print(f'A soma dos valores positivos é = {soma_positivo}')
