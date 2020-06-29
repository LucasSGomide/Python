from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub  # modulo de mesmo nome
# utiliza-se o AS para dar um "apelido" e resolver o conflito

print(f'Soma= {modulo1.soma(1,5)}')
print(f'Subtracao= {modulo1_sub.subtracao(7, 3)}')
