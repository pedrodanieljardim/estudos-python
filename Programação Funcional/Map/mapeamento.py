from data1 import produtoA,pessoasA,listaA

def aumentaPreco (produto):
    produto['preco'] = produto['preco'] * 1.05
    return produto

def aumentaPreco2 (produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto

novaLista = map(lambda x: x*2, listaA)

print('==================================================================')
print('ListaA = {}'.format(listaA))
print('novaLista (sem cast para lista) = {}'.format(novaLista))
print('novaLista (com cast para lista) = {}'.format(list(novaLista)))
print('==================================================================')

for produto in produtoA:
    print(produto)

print('==================================================================')

listaPreco = map(aumentaPreco,produtoA)
for preco in listaPreco:
    print(preco)

print('==================================================================')

listaPreco2 = map(aumentaPreco2,produtoA)
for preco2 in listaPreco2:
    print(preco2)