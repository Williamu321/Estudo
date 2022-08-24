''' Composição '''
from classe import Cliente

cliente1 = Cliente('Will', 32)
cliente1.insere_endereço('João pessoa', 'PB')
print(cliente1.nome)
cliente1.lista_enderecos()
print()
del cliente1

cliente2 = Cliente('Cinthia', 23)
cliente2.insere_endereço('Itabaiana', 'PB')
cliente2.insere_endereço('Sei la onde', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()
cliente3 = Cliente('Vanusa', 51)
cliente3.insere_endereço('Itabaiana', 'PA')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()


print('########################################################')