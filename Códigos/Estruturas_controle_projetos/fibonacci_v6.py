#! Python


def fibonacci(qnt):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == qnt:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(50):
        print(fib)
