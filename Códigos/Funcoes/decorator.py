def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log  # Retorna o decorator
def soma(a, b):
    return a + b


@log
def soma_quadrado(a, b):
    soma = a + b
    quadrado_soma = soma ** soma
    return quadrado_soma


(soma(2, 3))
(soma_quadrado(2, b=3))
