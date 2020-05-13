
d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

v = d1.copy()
v[1] = 'g'

print("Dicionário d1: {}".format(d1))
print("variável v: {}".format(v))
print('======================================================')
listaA = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
    ['c4', 4],
]
d2 = dict(listaA)

print("ListaA: {}".format(listaA))
print("Dicionário d2: {}".format(d2))

print('======================================================')

tuplaA = (
    ('a1', 1),
    ('a2', 2),
    ('a3', 3),
    ('a4', 4),
)
d3 = dict(tuplaA)

print("TuplaA: {}".format(tuplaA))
print("Dicionário d3: {}".format(d3))
