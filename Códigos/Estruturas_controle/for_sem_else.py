#! Python

PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'Eu falo sobre política e futebol',
    'Maria não gosta de nenhum dos assuntos proibidos',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'Texto possui pelo menos uma palavra proíbida: {palavra}')
            found = True
            break

    if not found:
        print('Texto autorizado: ', texto)

# for texto(string) - no caso cada uma das frases da lista TEXTOS
# for palavra (cada palavra) do(in) texto(cada string)
