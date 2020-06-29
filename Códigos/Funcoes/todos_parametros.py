def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # todos_params(primeiro='Joao', 'ana') não é possível args posicional deve
    # sempre vir antes de kwargs nomeado
    todos_params(primero='João', segundo='Ana')  # Opção 1 para problema acima
    todos_params('Maria', primeiro='João')  # Opção 2 para problema acima5
