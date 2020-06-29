# class Data:   Cração de uma classe (Tipo de dado personalizado) molde
#    def to_str(self):   Toda função(método) começa com SELF
#        return(f'{self.dia}/{self.mes}/{self.ano}')
# Agora criar objetos a partir da classe DATA


class Data:  # Cração de uma classe (Tipo de dado personalizado) molde
    def __str__(self):  # Toda função(método) começa com SELF
        return(f'{self.dia}/{self.mes}/{self.ano}')
# Agora criar objetos a partir da classe DATA


d1 = Data()  # Objeto D1
d1.dia = 5  # Em python é possível atribuir d1.dia -> Instância
d1.mes = 10  # parâmetros desta forma mesmo d1.mes -> Instância
d1.ano = 2019  # que eu não tenha atribuido na classe. d1.ano -> Instância

print(d1)  # Não preciso chamar a função pois é padrão python __str__
# print(d1.to_str())  # SELF = d1

d2 = Data()  # Objeto D1
d2.dia = 18  # Em python é possível atribuir d2.dia -> Instância
d2.mes = 10  # parâmetros desta forma mesmo d2.mes -> Instância
d2.ano = 1992  # que eu não tenha atribuido na classe d2.ano -> Instância

print(d2)  # Não preciso chamar a função pois é padrão python __str__
# print(d2.to_str())  # SELF = d2
