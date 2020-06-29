a = 3
b = 2
operacao = '*'


def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '/':
        return a / b
    elif operacao == '*':
        return a * b


print(calculadora(a, b, operacao))
