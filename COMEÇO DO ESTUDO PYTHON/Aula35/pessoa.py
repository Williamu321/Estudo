from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    
    def __init__(self, nome, idade,  feedando=False, falando = False):
        self.nome = nome
        self.idade = idade
        self.feedando = feedando
        self.falando = falando 



    def falar(self, assunto):
        if self.feedando:
            print(f'{self.nome} Não consegue falar enquanto feeda')
            return
        if self.falando:
            print(f'{self.nome} ja esta reclamando.')
            return
        
        print(f'{self.nome} Ta reclamando: {assunto})')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta reclamando')
            return
        print(f'{self.nome} parou de reclamar')
        self.falando = False
   
    def feedar(self, alimento):
        if self.feedando:
            print(f'{self.nome} Ja feedou pra caralho, tem nem como feedar mais.')
            return

        if self.falando:
            print(f'{self.nome} não pode feedar enquanto fica afk reclamando')
            return

        print(f'{self.nome} está feedando {alimento} pra caralho.')
        self.feedando = True

    def parar_feedar(self):
        if not self.feedando:
            print(f'{self.nome} Não esta feedando')
            return
        
        print(f'{self.nome} So parou de feedar por que a partida terminou.')
        self.feedando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
