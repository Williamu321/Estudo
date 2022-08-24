'''
Funções (def) em Python - return - Aula 16 (Parte2)
'''
'''def funcao(var):
    return var
    print('Isso não sera executado')

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor') 
'''

'''def divisao(n1, n2):

    if n2 == 0:
        return
    return n1 / n2
divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Conta invalida')
'''

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
var('Pode imprimir algo na tela')


def dumb():
    return ('Will', 'Merencio')
var = dumb()
print(var, type(var))
