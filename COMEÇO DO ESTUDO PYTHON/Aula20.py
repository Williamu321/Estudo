'''
Dicionários em Python
'''
# d1 = {'chave1':'valor da chave'}
# d1 =dict(chave1='Valor da chave', chave2 ='Valor da outra chave')
# d1['nova_chave'] = 'Valor da nova chave'
# d1 = { 1: 'Valor', 2 : 'Valor', 3 : 'Valor da real chave', }
# print(d1[3])

'''d1 = {
    'chave1': 'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tuplá',
}

for k, v in d1.items():
    print(k, v)
    '''

'''clientes = {
    'cliente1' : {
        'nome': 'Will',
        'sobrenome' : 'Merencio'
    },
    'cliente2' : {
        'nome' : 'cinthia',
        'sobrenome' : 'coelho'
    },
    'cliente3' : {
        'nome' : 'Sophia',
        'sobrenome' : 'alves'
    },
}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
        '''
        
import copy

'''d1 = {1: 'a', 2: 'b', 3:'c', 'd' : ['Will', 'Merencio']}
v = copy.deepcopy(d1)

v[1] = 'Will'
v['d'][0] = 'Cinthia'

print(d1)
print(v)
'''

d1 = {
    1: 2,
    2: 3,
    4: 6
}

d2 = {
    'a': 'b',
    'c': 'd',
}

d1.update(d2)
print(d1)
