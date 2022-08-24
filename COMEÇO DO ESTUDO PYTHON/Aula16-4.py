'''variavel = 'valor'

def func():
    print(variavel)

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()
outra_variavel = func2(arg=variavel)
print(outra_variavel)
'''

def func():
    outra_variavel = 'Will merencio'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)