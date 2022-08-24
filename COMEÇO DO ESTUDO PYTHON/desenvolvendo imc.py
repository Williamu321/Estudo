'''AULA 2
'''
nome = input('Seu nome')
idade = input('sua idade')  # int
ano_de_nascimento = 2022 - int(idade)
altura = input('sua altura')
peso = input('seu peso')
data_atual = '21/06/2022'

# Formula IMC = peso dividido pelo quadrado da altura
indice_massa_corporal = int(peso) / float(altura) ** 2
indice_massa_corporal = '{:0.3}' .format(indice_massa_corporal)
indice_massa_corporal = float(indice_massa_corporal)
print(f'{nome} tem {idade} anos nasceu no ano de {ano_de_nascimento} e seu IMC é de {indice_massa_corporal} ')
limite_imc = 22
if int(limite_imc) <= indice_massa_corporal:
    print('voce ta goido(a), va comer fruta e malhar seu(sua) mielda')
else : 
   print('você ta tranquila') 
