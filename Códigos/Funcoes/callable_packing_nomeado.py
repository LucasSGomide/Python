def calc_prec_final(prec_bruto, imposto, **parms):  # Packing parms
    return prec_bruto + prec_bruto * imposto(**parms)  # Unpacking
    # (preco bruto) + (preco bruto * impostos)


def imposto_x(importado):  # Se for importado retorna 0.23
    return 0.23 if importado else 0.11


def imposto_y(explosivo, fator=1):  # Se for explosivo retorna 0.11 * fator
    return 0.11 * fator if explosivo else 0


if __name__ == '__main__':
    preco_final = calc_prec_final(183.96, imposto_x, importado=True)
    preco_final = calc_prec_final(preco_final, imposto_y, explosivo=True,
                                  fator=1.2)
    print(f'Valor corrigido R${round(preco_final, 2)}')
