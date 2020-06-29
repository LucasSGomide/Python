#! Python


def fibonacci(qnt, lista=(0, 1)):
    return lista if len(lista) == qnt else \
        fibonacci(qnt, lista + (sum(lista[-2:]),))


if __name__ == "__main__":
    for fib in fibonacci(20):
        print(fib)
