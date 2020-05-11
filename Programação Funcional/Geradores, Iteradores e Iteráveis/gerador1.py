import sys
import time


def gera():
    r = []
    for n in range(100):
        r.append(n)
    return r


def gera2():
    for n in range(100):
        yield n
        time.sleep(0.1)


listaA = list(range(10))

print('ListaA : {}'.format(listaA))
print('Quantidade de bytes gastos na execução de ListaA: {}'.format(sys.getsizeof(listaA)))

listaB = list(range(100))

print('ListaB : {}'.format(listaB))
print('Quantidade de bytes gastos na execução de ListaB: {}'.format(sys.getsizeof(listaB)))

listaC = list(range(1000))

print('ListaC : {}'.format(listaC))
print('Quantidade de bytes gastos na execução de ListaC: {}'.format(sys.getsizeof(listaC)))

g = gera()
#   print('Laço For:')
#   for i in range(0, 100, 1):
#    print(g[i])

n = gera2()
print('variável n é um interável: {}'.format(hasattr(n, '___iter___')))
print('variável n é um interador: {}'.format(hasattr(n, '___next___')))
