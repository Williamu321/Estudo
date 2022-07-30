# %%
'''Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* enumerate - Enumerar elementos da lista # list / iteráveis
'''

string = 'O Brasil é o o o o pais do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')


for valor in lista_2:
    print(valor.strip().capitalize())
    
                                  