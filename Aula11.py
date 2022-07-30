'''Listas em Python
fatiamento
append, inser, pop, del, clear, extend, +
 min, max
range
'''

secreto = 'perfume'
digitadas =[]
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUU a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFF: a letra "{letra}" NÃO EXISTE na palavra secreta' )
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')

       






'''l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de é {type(elem)} e sey valor é {elem}')
'''


