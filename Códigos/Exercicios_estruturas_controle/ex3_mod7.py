a = []
b = []

limite = 0

while limite < 10:
    a.append(float(input('Insira um Número: ')))
    limite = limite + 1

for numeros in a:
    numeros = numeros ** 2
    b.append(numeros)

print(a)
print(b)
