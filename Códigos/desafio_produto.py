class Produto:
    def __init__(self, produto, valor, desconto):
        self.produto = produto
        self.valor = valor
        self.desconto = desconto
        self.valor_com_desconto = 0

    def calculadora_desconto(self):
        valor = self.valor
        desconto = self.desconto / 100
        produto = self.produto
        valor_com_desconto = valor - (valor * desconto)
        return f'{produto} de -> R${valor} por -> R${valor_com_desconto}'


if __name__ == '__main__':
    p1 = Produto('Placa de Video Radeon RX', 1500, 10)

    print(p1.calculadora_desconto())
