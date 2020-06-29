a = 6
b = 5
c = 4


def triangulo(a, b, c):
    check_1 = a + b > c
    check_2 = b + c > a
    check_3 = c + a > b
    if check_1 and check_2 and check_3 is True:
        if a == b == c:
            return('Equilatero')
        elif a == b != c:
            return('Isoceles')
        elif a == c != b:
            return('Isoceles')
        elif b == c != a:
            return('Isoceles')
        elif a != b != c:
            return('Escaleno')
    else:
        return('Nao e triangulo !')


print(triangulo(a, b, c))
