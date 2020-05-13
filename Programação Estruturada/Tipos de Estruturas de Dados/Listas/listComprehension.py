listaA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaB = [x for x in listaA]
# coloca valores da listaA para lista B
print('ListaB: {}'.format(listaB))

# dobra valores da listaA para listaC
listaC = [v * 2 for v in listaA]

print('ListaC: {}'.format(listaC))

listaD = ['Pedro', 'Martha', 'Jordan', 'Mike']

print('ListaD: {}'.format(listaD))

listaE = [x.replace('a', '@') for x in listaD]

print('ListaE: {}'.format(listaE))

tuplaA = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)

listaF = [(x, y) for x, y in tuplaA]
print('ListaF: {}'.format(listaF))

listaG = list(range(100))
print('ListaG: {}'.format(listaG))