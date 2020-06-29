#! Python


def fibonacci(qnt):
    resultado = [0, 1]
    for _ in range(qnt - 2):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)
