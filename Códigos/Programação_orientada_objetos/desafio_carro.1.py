class Carro:
    def __init__(self, vel_max):
        self.vel_max = vel_max
        self.vel_atual = 0

    def acelerar(self, delta):
        self.vel_atual = (self.vel_atual + delta if self.vel_atual
                          < self.vel_max - delta else self.vel_max)
        return(self.vel_atual)

    def frear(self, delta):
        self.vel_atual = (self.vel_atual - delta if self.vel_atual - delta >= 0
                          else 0)
        return(self.vel_atual)


if __name__ == '__main__':
    c1 = Carro(180)  # Velocidade máxima(limite) frear(0)

    for _ in range(25):
        print(c1.acelerar(8))  # Acelerar de 8 em 8 e retorna velo atual

    for _ in range(10):
        print(c1.frear(delta=35))  # Frear de 20 em 20 e retorna a 0