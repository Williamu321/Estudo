'''For ; Else em python'''

variavel = ['Will merencio', 'Cinthinha', 'Yasmin']

comeca_com_C = False
for valor in variavel:
    if valor.lower().startswith('c'):
        comeca_com_C = True
    

if comeca_com_C:
    print('Existe uma palavra que começa com c')
else:
    print('Não existe uma palavra que começa com c') 