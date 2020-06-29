# generator = (expressão for item in list if condicional)
# Generator -> Ocupa muito menos memoria e fornece valores
# sob demanda. print(next(generator))

generator = (i ** 2 for i in range(10) if i % 2 == 0)

for n in generator:
    print(n)
