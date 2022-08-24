import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    #Dólar: {cotacao_dolar}
    #Euro: {cotacao_euro}
    #BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto




janela = Tk()
janela.title('Cotação Atual das Moedas')
janela.geometry("400x500")


texto_orientação = Label(janela, text='Clique no botão para ver as cotações da moeda')
texto_orientação.grid(column=0, row=0, padx=60, pady=60)


botao = Button(janela, text= 'Buscar cotações Dolar/Euro/BTC', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=60, pady=60)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=60, pady=60)

janela.mainloop()


'''digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primeiro = (digitos[2])
segundo = primeiro
terceiro = (segundo + 1)
quarto = terceiro

senha = [
    input('Coloque a senha'),
    input('Coloque a senha'),
    input('Coloque a senha'),
    input('Coloque a senha'),
]

senha = list(senha)
print(senha)


if senha == ['3', '3', '4', '4']:
    print('recompensa adquirida')
else:
    print('tente novamente')'''
