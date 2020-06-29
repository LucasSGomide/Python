#! Python

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'Eu falo sobre política e futebol',
    'Maria não gosta de nenhum dos assuntos proibidos',
]

for texto in textos:
    intersect = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersect:
        print('Texto contem palavras proibidas: ', intersect)
    else:
        print('Texto liberado: ', texto)
