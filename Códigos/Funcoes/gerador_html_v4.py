# Gerador de tag HTML
# Parâmetros Nomeados exemplos de como usar !


def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):  # Será criada uma tupla com os dados inseridos
    lista = ''.join((f'<li>{item}</li>' for item in itens))  # generator
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('span', classe='inline', inline=True))
    print(tag_bloco('div pra dividir um bloco'))
    print(tag_bloco('span para escrever na msma liha', inline=True))
    print(tag_bloco(inline=True, conteudo='span para escrever na msma liha'))
    print(tag_bloco('Falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    # chama a função
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo',  # Não chama a função
                    classe='info', inline=True))  # tag_lista como *args
