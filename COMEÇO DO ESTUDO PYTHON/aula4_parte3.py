'''operadores logicos 
and, or, no, in, not in'''

'''VERDADEIRO E VERDADEIRO - AS DUAS TEM QUE SER VERDADEIRAS
 Comparação1 and comparação 2
 
 VERDADEIRO OU VERDADEIRO - QUALQUER UMA QUE FOR VERDADEIRO EXPRESSÃO = TRUE
 comp1 or comp2

OPERADOR NOT INVERTE O VALOR

a=2 
b=3
if not b>a:
    print('B é maior que a')
else:
    print('A é maior que B')

#OPERADOR IN
nome = 'will' #SE EXISTE ALGO DENTRO DA VARIAVEL NOME COMO SABER AS LETRAS QUE TEM.

if 'a' in nome:
    print('existe a letra i no seu nome')
else:
    print('não existe')

#OPERADOR NOT IN 
nome = 'william'
 
if 'illi' not in nome:
    print('executar')
else:
    print('Não executar')
'''


nome = input('Qual o seu nome')
idade = input('Qual a sua idade')

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} não pode pegar o emprestimo')

