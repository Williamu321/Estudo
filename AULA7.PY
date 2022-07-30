'''while False:
    nome = input('qual o seu nome')
    print(f'olá {nome}')
print('Não sera executada')
'''
'''x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1
print('Acabou')
'''
x = 0 # coluna


'''while x < 10:
    y = 0 # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1 # x = x + 1

print('acabou')
'''

while True:
    print()
    num_1 = input('digite um numero')
    num_2 = input('digite outro numero')
    operador = input('digite um operador')
    

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um numero.') 
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido')
        
        break
    10