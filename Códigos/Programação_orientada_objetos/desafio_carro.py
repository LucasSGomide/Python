velocidade = 0


class Carro:
    def __init__(self, vel_max):
        self.vel_max = vel_max

    def acelerar(self, delta=5):
        global velocidade
        self.delta = delta
        if velocidade < self.vel_max - delta:
            velocidade += delta
            return(f'Acelerando..{velocidade}km/h')
        elif velocidade in range(self.vel_max - delta, self.vel_max):
            velocidade = 180
            return(f'Velocidade maxima atingida= {velocidade}km/h')
        elif velocidade == self.vel_max:
            return f'Limite do motor..'

    def frear(self, delta=5):
        global velocidade
        self.delta = delta
        if velocidade >= delta:
            velocidade -= delta
            return f'Freando.. {velocidade}km/h'
        elif velocidade in range(1, delta):
            velocidade = 0
            return f'Carro parado com sucesso.. {velocidade}km/h'
        elif velocidade == 0:
            return f'Carro parado {velocidade}km/h <Limite de frenagem>'


if __name__ == '__main__':
    c1 = Carro(180)  # Velocidade máxima(limite) frear(0)

    for _ in range(25):
        print(c1.acelerar(8))  # Acelerar de 8 em 8 e retorna velo atual

    for _ in range(10):
        print(c1.frear(delta=20))  # Frear de 20 em 20 e retorna a 0
