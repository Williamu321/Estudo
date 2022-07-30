usuario = input('Nome de usuario')
senha = input('Senha do usuario')

usuario_bd = 'will'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha invalido')
    