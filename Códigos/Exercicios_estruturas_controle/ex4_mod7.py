a = []
limite = 0

while limite < 8:
    a.append(int(input('Digite um valor: ')))
    limite = limite + 1
    continue
x = int(input('Digite o valor de X (1 a 7): '))
y = int(input('Digite o valor de Y (1 a 7): '))


x = a[x]
y = a[y]

print(f'soma de {x} + {y} é = ', x + y)
