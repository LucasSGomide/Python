def fibonacci(sequencia=[0, 1]):
    # Uso de LISTA/Mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))


def fibonacci_2(sequencia=(0, 1)):
    # Solução possível
    return (sequencia) + (sequencia[-1] + sequencia[-2],)


if __name__ == '__main__':
    inicio = fibonacci_2()
    print(inicio, id(inicio))
    print(fibonacci_2(inicio))
    restart = fibonacci_2()
    print(restart, id(restart))
