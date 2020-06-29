# Gerador de tag HTML
# Parâmetros posicionais, exemplos de uso.


def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (Assertions)
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'
    assert tag_bloco('Impossível excluir', 'error') == \
        '<div class="error">Impossível excluir</div>'

print(tag_bloco('Teste HTML', 'teste'))
