listaA = [1, 2, 3, 4, 5, 6, 7]

# verificando se uma variável é um interador
print('variável listaA é um interador: {}'.format(hasattr(listaA, '___next___')))

# transformando uma variável em um interável, podendo assim usar o método next...
listaA = iter(listaA)
print('interando a variável:')
print(next(listaA))
print(next(listaA))
print(next(listaA))
print(next(listaA))
print(next(listaA))

