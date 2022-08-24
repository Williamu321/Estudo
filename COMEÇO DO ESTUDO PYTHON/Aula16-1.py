'''
Funções - def em Python (Parte 1)
'''
'''def saudação(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudação()
saudação(nome='zezinho', msg='Hi')
saudação('Olá', 'Will')
saudação('Oi', 'Cinthia')
saudação('Hello', 'Henry')
saudação('Olá', 'Sophia')
'''
def saudação(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudação()

print(variavel)
