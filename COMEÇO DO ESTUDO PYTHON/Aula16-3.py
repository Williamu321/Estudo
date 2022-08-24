'''
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
'''
def func(*args, **kwargs):
    print(args)
    # print(kwargs['nome'], kwargs['sobrenome'])

    idade =kwargs['idade']
    print(idade)


lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Will', sobrenome='merencio', idade=30)

