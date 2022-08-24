'''
Geradores, iteradores e iteráveis em Python
'''

'''lista = [0,1,2,3,4,5]
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__')) '''


from audioop import lin2adpcm
import sys
import time

'''def gera():

   variavel = 'Valor 1'
   yield variavel
   variavel = 'Valor 2'
   yield variavel
   variavel = 'Valor 3'
   yield variavel

g = gera()

for v in g:
    print(v)

'''

l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))
for v in l2:
    print(v)