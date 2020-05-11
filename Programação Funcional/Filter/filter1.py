from data import produtoA, pessoasA, listaA

novaLista1 = filter(lambda x: x >= 5, listaA)
# filter funciona como literalmente um filtro na lista....

print('==================================================================')
print('ListaA = {}'.format(listaA))
print('novaLista (sem cast para lista) = {}'.format(novaLista1))
print('novaLista (com cast para lista) = {}'.format(list(novaLista1)))
print('==================================================================')

novaLista2 = filter(lambda p:p['preco'] > 50, produtoA)

print('==================================================================')
print('ProdutoA = {}'.format(produtoA))
print('novaLista2 (sem cast para lista) = {}'.format(novaLista2))
print('novaLista2 (com cast para lista) = {}'.format(list(novaLista2)))
print('==================================================================')