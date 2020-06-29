class Data:
    def __init__(self, dia, mes, ano):  # Construtor que recebe 3 parametros
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return(f'{self.dia}/{self.mes}/{self.ano}')


d1 = Data(5, 10, 2019)  # OBJ instanciado a partir de um construtor
# d1.dia = 5
# d1.mes = 10
# d1.ano = 2019

print(d1)

d2 = Data(18, 10, 1992)
# d2.dia = 18
# d2.mes = 10
# d2.ano = 1992

print(d2)
