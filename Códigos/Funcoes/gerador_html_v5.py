# Gerador de tag HTML
# Parâmetros Nomeados exemplos de como usar !
bloco_atrs = ('bloco_acsseskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))  # generator
    atributos = filtrar_atrs(novos_atrs, ul_atrs)
    return f'<ul {atributos} >{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco('span', classe='inline', inline=True))
    # print(tag_bloco('div pra dividir um bloco'))
    # print(tag_bloco('span para escrever na msma liha', inline=True))
    # print(tag_bloco(inline=True, conteudo='span para escrever na msma liha'))
    # print(tag_bloco('Falhou', classe='error'))
    # print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    # chama a função
    # print(tag_bloco(tag_lista, 'Sabado', 'Domingo',  # Não chama a função
    #                classe='info', inline=True))  # tag_lista como *args
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_acsseskey='m', bloco_id='conteudo',
                    ul_id='lista', ul_style='color:red'))
