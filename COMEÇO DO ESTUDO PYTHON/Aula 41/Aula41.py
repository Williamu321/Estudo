''' Associação '''
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Will')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
