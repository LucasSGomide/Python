class Carro:
    def __init__(self, vel_max):  # Construtor
        self.vel_max = vel_max  # Atributo
        self.vel_atual = 0  # Atributo

    def acelerar(self, delta=5):  # Comportamento
        maxima = self.vel_max
        nova = self.vel_atual + delta
        self.vel_atual = nova if nova <= maxima else maxima
        return self.vel_atual

    def frear(self, delta=5):  # Comportamento
        nova = self.vel_atual - delta
        self.vel_atual = nova if nova >= 0 else 0
        return self.vel_atual


if __name__ == '__main__':
    c1 = Carro(180)  # Velocidade máxima(limite) frear(0)

    for _ in range(25):
        print(c1.acelerar(8))  # Acelerar de 8 em 8 e retorna velo atual

    for _ in range(10):
        print(c1.frear(delta=20))  # Frear de 20 em 20 e retorna a 0
