# https://docs.python.org/3/library/functions.html#open
''' Como criar, ler e escrever arquivos com Python'''
'''
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('#############')

file.seek(0, 0)

print(file.readline(), end = '')
print(file.readline(), end = '')
print(file.readline(), end = '')
print('##########')

file.seek(0, 0)

for linha in file:
    print(linha, end='') #o end = '' serve para não aplciar a quebra de linha

file.close()
'''
with open('abc.txt', 'w+') as file: # melhor maneira de trabalhar em python
     file.write('Outra linha\n')
     file.seek(0)
     print(file.read())
# import os # para remover o arquivo
# os.remove('abc.txt')
    











