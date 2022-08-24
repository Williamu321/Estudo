from tkinter import *


def senha_Correta():

    mensagem = f'Resposta certa'
    texto = f'''{mensagem}'''

    texto_resposta["text"] = texto

def senha_errada1():
    mensagem = f'Resposta errada'
    texto = f'''{mensagem}'''

    texto_resposta["text"] = texto

def senha_errada2():
    mensagem = f'Resposta errada'
    texto = f'''{mensagem}'''

    texto_resposta["text"] = texto

def senha_errada3():
    mensagem = f'Resposta errada'
    texto = f'''{mensagem}'''

    texto_resposta["text"] = texto


janela = Tk()
janela.title('Pergunta')


texto_orientação = Label(janela, text='O primeiro e o segundo são iguais, o terceiro e o quarto tambem são iguais, o terceiro é maior em 1 que o segundo,o primeiro é maior que 1 e o quarto é menor que 5, o segundo não pode ser um numero par')
texto_orientação.grid(column=0, row=0, padx=10, pady=10)


botao = Button(janela, text= 'A: 3, 3, 4, 4', command=senha_Correta)
botao.grid(column=0, row=5, padx=10, pady=10)
botao = Button(janela, text= 'B: 2, 3, 2, 4', command=senha_errada3)
botao.grid(column=0, row=6, padx=10, pady=10)
botao = Button(janela, text= 'C: 1, 1, 2, 2', command=senha_errada2)
botao.grid(column=0, row=7, padx=10, pady=10)
botao = Button(janela, text= 'D: 1, 2, 3, 4', command=senha_errada1)
botao.grid(column=0, row=8, padx=10, pady=10)
    
texto_resposta = Label(janela, text='')
texto_resposta.grid(column=0, row=9, padx=10, pady=10)
janela.mainloop()
