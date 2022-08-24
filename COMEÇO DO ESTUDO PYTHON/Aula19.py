'''
Trocando o valor entre variáveis em Python
'''

x = 10 # Will
y = 'Will' # 10
z = 'Cinthia'

x, y, z = z, x, y

a = [x, y, z]
for v in a:
    print(v)

