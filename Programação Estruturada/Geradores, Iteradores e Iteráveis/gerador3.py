import sys
import time

listaA = [x for x in range(10000)]

print('ListaA: {}'.format(listaA))
print('Tipo de ListaA: {}'.format(type(listaA)))
print('====================================================')

listaA = (x for x in range(10000))

print('ListaA: {}'.format(listaA))
print('Tipo de ListaA: {}'.format(type(listaA)))

listaC = [x for x in range(10000)]
listaD = (x for x in range(10000))

print('====================================================')
print('Tamanho de listaC: {}'.format(sys.getsizeof(listaC)))
print('Tamanho de listaD: {}'.format(sys.getsizeof(listaD)))