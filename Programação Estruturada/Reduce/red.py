from data import produtoA, pessoasA, listaA
from functools import reduce

acumula = 0

for item in listaA:
    acumula += item

print("Acumulando valores com o for: {}".format(acumula))


somaLista = reduce(lambda ac, i: i +ac, listaA, 0)
print('Acumulando valores com a função reduce: {}'.format(somaLista))
