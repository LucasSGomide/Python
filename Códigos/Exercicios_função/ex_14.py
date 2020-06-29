def consumo_gas(km, litros):
    km_l = km/litros
    if km_l < 8:
        return(f'{km_l}km/l = Venda o carro')
    elif km_l in range(8, 15):
        return(f'{km_l}km/l = Economico !')
    elif km_l > 12:
        return(f'{km_l}km/l = Super Economico !')


print(consumo_gas(400, 50))