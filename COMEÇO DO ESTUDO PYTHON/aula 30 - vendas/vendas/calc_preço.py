from vendas.formata import preço

def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return preço.real(r)
    else:
        return r

def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))

    if formata:

        return preço.real(r)
    else:
        return r
    



