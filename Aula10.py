'''For in em Python
Iterando strungs com for
Função range (start = 0. stop. step=1)
'''

'''for n in range(0, 100, 8):
    print(n)
print('################')
for n in range(100):
    if n % 8 == 0:
        print(n)
        '''
    

#continue - pula para o proximo laço
#break   - termina o laço
texto ='Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)