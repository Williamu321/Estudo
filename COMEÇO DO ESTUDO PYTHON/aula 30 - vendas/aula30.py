
from vendas.calc_preço import aumento, reducao
import vendas.formata.preço as preço2

preco = 20
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco, porcentagem=25, formata=True)
print(preco_com_reducao)

print(preço2.real(20))

