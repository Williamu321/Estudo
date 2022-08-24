'''Iterando string com while em python'''
minha_string = 'o rato roeu a roupa do rei de roma.'#indice 35
tamanho_string = len(minha_string)

c = 0
contagem_atual = 0
letra = ''

while c < tamanho_string:
    qtd_vezes_letra = minha_string.count(minha_string[c])
    if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
        letra = minha_string[c]
        contagem_atual = qtd_vezes_letra
    #print(minha_string[c], conta)

    c += 1
print(letra, contagem_atual)

