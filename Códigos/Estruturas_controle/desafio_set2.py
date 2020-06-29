PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = {
    'Eu falo sobre política e futebol',
    'Maria não gosta de nenhum dos assuntos proibidos',
}

for texto in textos:
    contem = PALAVRAS_PROIBIDAS.__contains__(set(texto.lower().split()))
    if contem:
        print('Texto não autorizado: ', contem)
    else:
        print('Texto Autorizado:', texto)
