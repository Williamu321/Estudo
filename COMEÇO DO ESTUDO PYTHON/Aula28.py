# Módulos padrão em Python:
# Módulos são arquivos .py (que contem código em ptyhon) e serven
# para expandir as funcionalidades padrão da linguagem.
# veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

'''
from sys import platform, audit as so, au
print(so)
'''
from random import randint as randint_original
#import random
def randint(*args):
    return 'hahaha'

for i in range(10):
    print(randint_original(0,10))
    #print(random.randint(0,10))
print(randint())
