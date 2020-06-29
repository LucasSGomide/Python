# Gerador de tag HTML
# Parâmetros Nomeados exemplos de como usar !


def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('span', 'inline', True))
    print(tag_bloco('div pra dividir um bloco'))
    print(tag_bloco('span para escrever na msma liha', inline=True))
    print(tag_bloco(inline=True, texto='span para escrever na msma liha'))
    print(tag_bloco('Falhou', classe='error'))
