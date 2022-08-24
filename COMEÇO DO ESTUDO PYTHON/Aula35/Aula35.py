'''Classes - Python Orientando a Objetos'''

from pessoa import Pessoa

p1 = Pessoa('guilherme', 35)
p2 = Pessoa('Jadan', 52)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


p1.feedar('yasuo')
p2.falar('"Puta merda guilherme para de feedar essa porra"')
p1.parar_feedar()
p1.falar('que yasuo tava absudo de forte')
p2.parar_falar()
p2.falar('POR QUE SERA NE GUILHERME, POR QUE SERA FILHA DA PUTA!!!!')


#




